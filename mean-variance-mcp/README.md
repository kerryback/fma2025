# Mean-Variance Portfolio Optimizer MCP Extension

A Claude Desktop extension for portfolio optimization using mean-variance analysis.

## Installation

### Step 1: Install Python Dependencies

Before installing the extension in Claude Desktop, install the required Python packages:

```bash
pip install mcp numpy
```

Or if you prefer using the requirements file:

```bash
pip install -r server/requirements.txt
```

### Step 2: Install the Extension

1. Open Claude Desktop
2. Go to **Settings > Extensions**
3. Click **"Install from file"**
4. Select the `mean-variance-mcp.mcpb` file
5. Click **Install**

## Usage

Once installed, you can ask Claude to perform portfolio optimization:

### Example 1: Tangency Portfolio

```
Calculate the tangency portfolio for 3 assets:
- Expected returns: 10%, 12%, 8%
- Standard deviations: 15%, 20%, 12%
- Correlation matrix:
  [[1.0, 0.3, 0.2],
   [0.3, 1.0, 0.4],
   [0.2, 0.4, 1.0]]
- Risk-free rate: 3%
```

### Example 2: Minimum Variance Portfolio

```
Find the minimum variance portfolio for 2 assets:
- Standard deviations: 20%, 25%
- Correlation: 0.5
```

## Tools Provided

### `calculate_tangency_portfolio`
Calculates the portfolio with the highest Sharpe ratio (tangency portfolio on the efficient frontier).

**Inputs:**
- `means`: Expected returns for each asset (as decimals)
- `stds`: Standard deviations for each asset (as decimals)
- `correlations`: NxN correlation matrix (symmetric with 1s on diagonal)
- `risk_free_rate`: Risk-free rate of return (as decimal)

**Outputs:**
- Portfolio weights
- Expected return
- Volatility (standard deviation)
- Sharpe ratio

### `calculate_minimum_variance_portfolio`
Calculates the portfolio with the lowest possible volatility.

**Inputs:**
- `stds`: Standard deviations for each asset (as decimals)
- `correlations`: NxN correlation matrix (symmetric with 1s on diagonal)

**Outputs:**
- Portfolio weights
- Volatility (standard deviation)

## Technical Details

- **Language**: Python 3
- **Dependencies**: mcp, numpy
- **License**: MIT
- **Author**: Kerry Back

## Troubleshooting

### "No module named mcp" error

Make sure you've installed the Python dependencies:
```bash
pip install mcp numpy
```

### Extension not appearing in Claude

1. Restart Claude Desktop after installation
2. Check that the extension is enabled in Settings > Extensions
3. Verify the .mcpb file was installed successfully
