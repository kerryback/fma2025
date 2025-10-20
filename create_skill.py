import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 8)
ax.axis('off')

# Set light gray background
fig.patch.set_facecolor('lightgray')
ax.set_facecolor('lightgray')

# Node positions - DW moved to where MCP was, no MCP
nodes = {
    'User': (1, 4),
    'LLM': (5, 4),
    'DW': (5, 1)
}

# Node colors
node_colors = {
    'User': 'lightyellow',
    'LLM': 'lightyellow',
    'DW': 'lightyellow'
}

# Draw nodes as rounded rectangles
node_patches = {}
for name, (x, y) in nodes.items():
    if name == 'DW':
        # Two-line text for Data Warehouse
        width, height = 2.0, 0.8
        rect = FancyBboxPatch((x - width/2, y - height/2), width, height,
                              boxstyle="round,pad=0.3",
                              facecolor=node_colors[name],
                              edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y + 0.15, 'Data', ha='center', va='center', fontsize=18, fontweight='bold')
        ax.text(x, y - 0.2, 'Warehouse', ha='center', va='center', fontsize=18, fontweight='bold')
    else:
        # Single-line text for other nodes
        width = 1.7
        height = 0.6
        rect = FancyBboxPatch((x - width/2, y - height/2), width, height,
                              boxstyle="round,pad=0.3",
                              facecolor=node_colors[name],
                              edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=18, fontweight='bold')
    node_patches[name] = rect

# Two color scheme
color1 = '#1E90FF'  # Blue for User <-> LLM
color3 = '#FF6347'  # Red/Tomato for LLM <-> DW

# Helper function to create curved arrow
def draw_curved_arrow(ax, start, end, color, curve_height=0.5, above=True):
    x1, y1 = start
    x2, y2 = end

    # Calculate control point for curve
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2

    # Add curve
    if above:
        control_y = mid_y + curve_height
    else:
        control_y = mid_y - curve_height

    # Create curved arrow using FancyArrowPatch with connectionstyle
    # Note: For horizontal arrows, negative rad curves upward, positive curves downward
    if abs(x1 - x2) > abs(y1 - y2):  # Horizontal arrow
        if x1 < x2:  # Left to right
            connectionstyle = f"arc3,rad={-0.4 if above else 0.4}"
        else:  # Right to left
            connectionstyle = f"arc3,rad={0.4 if above else -0.4}"
    else:  # Vertical arrow
        connectionstyle = f"arc3,rad={0.3 if curve_height > 0 else -0.3}"

    arrow = FancyArrowPatch(start, end,
                           #connectionstyle=connectionstyle,
                           arrowstyle='->',
                           color=color, linewidth=3.5,
                           mutation_scale=25,
                           zorder=1)
    ax.add_patch(arrow)

# Draw arrows with proper curves and labels

# 1. User -> LLM (above)
draw_curved_arrow(ax, (nodes['User'][0] + 1.1, nodes['User'][1] + 0.3),
                 (nodes['LLM'][0] - 1.1, nodes['LLM'][1] + 0.3),
                 color1, curve_height=0.5, above=True)

# 2. LLM -> User (below)
draw_curved_arrow(ax, (nodes['LLM'][0] - 1.1, nodes['LLM'][1] - 0.3),
                 (nodes['User'][0] + 1.1, nodes['User'][1] - 0.3),
                 color1, curve_height=0.5, above=False)

# 3. LLM -> DW (curves right)
start_3 = (nodes['LLM'][0] + 0.5, nodes['LLM'][1] - 0.55)
end_3 = (nodes['DW'][0] + 0.5, nodes['DW'][1] + 0.6)
arrow_3 = FancyArrowPatch(start_3, end_3,
                         #connectionstyle="arc3,rad=-0.3",
                         arrowstyle='->',
                         color=color3, linewidth=3.5, mutation_scale=25, zorder=1)
ax.add_patch(arrow_3)

# 4. DW -> LLM (curves left)
start_4 = (nodes['DW'][0] - 0.5, nodes['DW'][1] + 0.65)
end_4 = (nodes['LLM'][0] - 0.5, nodes['LLM'][1] - 0.5)
arrow_4 = FancyArrowPatch(start_4, end_4,
                         #connectionstyle="arc3,rad=-0.3",
                         arrowstyle='->',
                         color=color3, linewidth=3.5, mutation_scale=25, zorder=1)
ax.add_patch(arrow_4)

# Create legend
legend_elements = [
    mpatches.Patch(color=color1, label='User ↔ LLM'),
    mpatches.Patch(color=color3, label='LLM ↔ Data Warehouse')
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=16, frameon=True, fancybox=True, shadow=True)

# Save the figure
plt.tight_layout()
plt.savefig('skill.png', dpi=300, bbox_inches='tight',
            facecolor='lightgray', edgecolor='none')
print("Diagram created as skill.png")
plt.close()
