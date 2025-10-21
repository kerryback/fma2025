import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np

# Create figure and axis with smaller dimensions
fig, ax = plt.subplots(1, 1, figsize=(6, 4.5))
ax.set_xlim(0.3, 5.2)
ax.set_ylim(0.9, 4.1)
ax.axis('off')

# Set transparent background
fig.patch.set_alpha(0.0)
ax.set_facecolor('none')

# Node positions - centered in the smaller background
nodes = {
    'User': (1.2, 3),
    'LLM': (4, 3),
    'DW': (4, 1.5)
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
        width, height = 1.4, 0.6
        rect = FancyBboxPatch((x - width/2, y - height/2), width, height,
                              boxstyle="round,pad=0.15",
                              facecolor=node_colors[name],
                              edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y + 0.12, 'Data', ha='center', va='center', fontsize=14, fontweight='bold')
        ax.text(x, y - 0.15, 'Warehouse', ha='center', va='center', fontsize=14, fontweight='bold')
    elif name == 'LLM':
        # Two-line text for LLM + Code Execution
        width, height = 1.6, 0.6
        rect = FancyBboxPatch((x - width/2, y - height/2), width, height,
                              boxstyle="round,pad=0.15",
                              facecolor=node_colors[name],
                              edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y + 0.12, 'LLM + Code', ha='center', va='center', fontsize=14, fontweight='bold')
        ax.text(x, y - 0.15, 'Execution', ha='center', va='center', fontsize=14, fontweight='bold')
    else:
        # Single-line text for other nodes
        width = 1.2
        height = 0.5
        rect = FancyBboxPatch((x - width/2, y - height/2), width, height,
                              boxstyle="round,pad=0.15",
                              facecolor=node_colors[name],
                              edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=14, fontweight='bold')
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
draw_curved_arrow(ax, (nodes['User'][0] + 0.75, nodes['User'][1] + 0.15),
                 (nodes['LLM'][0] - 0.9, nodes['LLM'][1] + 0.15),
                 color1, curve_height=0.5, above=True)

# 2. LLM -> User (below)
draw_curved_arrow(ax, (nodes['LLM'][0] - 0.95, nodes['LLM'][1] - 0.15),
                 (nodes['User'][0] + 0.7, nodes['User'][1] - 0.15),
                 color1, curve_height=0.5, above=False)

# 3. LLM -> DW (right side, vertical going down)
start_3 = (nodes['LLM'][0] + 0.4, nodes['LLM'][1] - 0.45)
end_3 = (nodes['DW'][0] + 0.4, nodes['DW'][1] + 0.4)
arrow_3 = FancyArrowPatch(start_3, end_3,
                         arrowstyle='->',
                         color=color3, linewidth=3.5, mutation_scale=25, zorder=1)
ax.add_patch(arrow_3)

# 4. DW -> LLM (left side, vertical going up)
start_4 = (nodes['DW'][0] - 0.4, nodes['DW'][1] + 0.45)
end_4 = (nodes['LLM'][0] - 0.4, nodes['LLM'][1] - 0.4)
arrow_4 = FancyArrowPatch(start_4, end_4,
                         arrowstyle='->',
                         color=color3, linewidth=3.5, mutation_scale=25, zorder=1)
ax.add_patch(arrow_4)

# Legend removed - diagram is now centered

# Save the figure
plt.tight_layout()
plt.savefig('skill_v2.png', dpi=300, bbox_inches='tight',
            facecolor='none', edgecolor='none', transparent=True)
print("Diagram created as skill_v2.png")
plt.close()
