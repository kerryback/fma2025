#!/usr/bin/env python3
"""
Mean-Variance Portfolio Optimization MCP Server
Provides tools for calculating optimal portfolios using modern portfolio theory.
"""

import asyncio
import numpy as np
from typing import Any
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import json


def calculate_tangency_portfolio(
    means: list[float],
    stds: list[float],
    correlations: list[list[float]],
    risk_free_rate: float
) -> dict[str, Any]:
    """
    Calculate the tangency portfolio weights using mean-variance optimization.

    Args:
        means: Expected returns for each asset
        stds: Standard deviations for each asset
        correlations: Correlation matrix between assets
        risk_free_rate: Risk-free rate of return

    Returns:
        Dictionary containing portfolio weights, expected return, and volatility
    """
    n = len(means)

    # Convert to numpy arrays
    mu = np.array(means)
    sigma_vec = np.array(stds)
    corr = np.array(correlations)

    # Compute covariance matrix from correlations and standard deviations
    # Cov[i,j] = corr[i,j] * std[i] * std[j]
    cov_matrix = np.outer(sigma_vec, sigma_vec) * corr

    # Excess returns
    excess_returns = mu - risk_free_rate

    # Calculate tangency portfolio weights
    # w = Σ^(-1) * (μ - rf) / 1'Σ^(-1)(μ - rf)
    try:
        inv_cov = np.linalg.inv(cov_matrix)
        weights = inv_cov @ excess_returns
        weights = weights / np.sum(weights)

        # Calculate portfolio metrics
        portfolio_return = np.dot(weights, mu)
        portfolio_variance = weights @ cov_matrix @ weights
        portfolio_std = np.sqrt(portfolio_variance)
        sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_std

        return {
            "weights": weights.tolist(),
            "expected_return": float(portfolio_return),
            "volatility": float(portfolio_std),
            "sharpe_ratio": float(sharpe_ratio),
            "success": True
        }
    except np.linalg.LinAlgError:
        return {
            "success": False,
            "error": "Covariance matrix is singular - cannot compute tangency portfolio"
        }


def calculate_minimum_variance_portfolio(
    stds: list[float],
    correlations: list[list[float]]
) -> dict[str, Any]:
    """
    Calculate the minimum variance portfolio weights.

    Args:
        stds: Standard deviations for each asset
        correlations: Correlation matrix between assets

    Returns:
        Dictionary containing portfolio weights and volatility
    """
    n = len(stds)

    # Convert to numpy arrays
    sigma_vec = np.array(stds)
    corr = np.array(correlations)

    # Compute covariance matrix
    cov_matrix = np.outer(sigma_vec, sigma_vec) * corr

    # Calculate minimum variance portfolio
    # w = Σ^(-1) * 1 / (1'Σ^(-1)1)
    try:
        inv_cov = np.linalg.inv(cov_matrix)
        ones = np.ones(n)
        weights = inv_cov @ ones
        weights = weights / np.sum(weights)

        # Calculate portfolio volatility
        portfolio_variance = weights @ cov_matrix @ weights
        portfolio_std = np.sqrt(portfolio_variance)

        return {
            "weights": weights.tolist(),
            "volatility": float(portfolio_std),
            "success": True
        }
    except np.linalg.LinAlgError:
        return {
            "success": False,
            "error": "Covariance matrix is singular - cannot compute minimum variance portfolio"
        }


# Create server instance
server = Server("mean-variance-optimizer")


@server.list_tools()
async def handle_list_tools() -> list[Tool]:
    """List available portfolio optimization tools."""
    return [
        Tool(
            name="calculate_tangency_portfolio",
            description=(
                "Calculate the tangency (maximum Sharpe ratio) portfolio given "
                "expected returns, standard deviations, correlations, and risk-free rate. "
                "Returns optimal portfolio weights, expected return, volatility, and Sharpe ratio."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "means": {
                        "type": "array",
                        "items": {"type": "number"},
                        "description": "Expected returns for each asset (as decimals, e.g., 0.10 for 10%)"
                    },
                    "stds": {
                        "type": "array",
                        "items": {"type": "number"},
                        "description": "Standard deviations for each asset (as decimals)"
                    },
                    "correlations": {
                        "type": "array",
                        "items": {
                            "type": "array",
                            "items": {"type": "number"}
                        },
                        "description": "Correlation matrix (NxN symmetric matrix with 1s on diagonal)"
                    },
                    "risk_free_rate": {
                        "type": "number",
                        "description": "Risk-free rate of return (as decimal, e.g., 0.03 for 3%)"
                    }
                },
                "required": ["means", "stds", "correlations", "risk_free_rate"]
            }
        ),
        Tool(
            name="calculate_minimum_variance_portfolio",
            description=(
                "Calculate the minimum variance portfolio given standard deviations "
                "and correlations. Returns optimal portfolio weights and volatility."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "stds": {
                        "type": "array",
                        "items": {"type": "number"},
                        "description": "Standard deviations for each asset (as decimals)"
                    },
                    "correlations": {
                        "type": "array",
                        "items": {
                            "type": "array",
                            "items": {"type": "number"}
                        },
                        "description": "Correlation matrix (NxN symmetric matrix with 1s on diagonal)"
                    }
                },
                "required": ["stds", "correlations"]
            }
        )
    ]


@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool execution requests."""

    if name == "calculate_tangency_portfolio":
        result = calculate_tangency_portfolio(
            means=arguments["means"],
            stds=arguments["stds"],
            correlations=arguments["correlations"],
            risk_free_rate=arguments["risk_free_rate"]
        )

        if result["success"]:
            output = f"""Tangency Portfolio Results:

Portfolio Weights:
{', '.join([f'Asset {i+1}: {w:.4f} ({w*100:.2f}%)' for i, w in enumerate(result['weights'])])}

Expected Return: {result['expected_return']:.4f} ({result['expected_return']*100:.2f}%)
Volatility (Std Dev): {result['volatility']:.4f} ({result['volatility']*100:.2f}%)
Sharpe Ratio: {result['sharpe_ratio']:.4f}
"""
        else:
            output = f"Error: {result['error']}"

    elif name == "calculate_minimum_variance_portfolio":
        result = calculate_minimum_variance_portfolio(
            stds=arguments["stds"],
            correlations=arguments["correlations"]
        )

        if result["success"]:
            output = f"""Minimum Variance Portfolio Results:

Portfolio Weights:
{', '.join([f'Asset {i+1}: {w:.4f} ({w*100:.2f}%)' for i, w in enumerate(result['weights'])])}

Volatility (Std Dev): {result['volatility']:.4f} ({result['volatility']*100:.2f}%)
"""
        else:
            output = f"Error: {result['error']}"
    else:
        output = f"Unknown tool: {name}"

    return [TextContent(type="text", text=output)]


async def main():
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="mean-variance-optimizer",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                )
            )
        )


if __name__ == "__main__":
    asyncio.run(main())
