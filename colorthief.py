import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

# Project: AI Orientalism Color Analysis
# Description: Visualizing the "yellow-brown" bias in AI-generated images.

def plot_color_grid_final(colors, names, cols=5):
    # Setup canvas
    n = len(colors)
    rows = math.ceil(n / cols)
    fig, ax = plt.subplots(figsize=(cols * 2.5, rows * 2.5))
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    
    # Draw grids
    for idx, (color, name) in enumerate(zip(colors, names)):
        col_idx = idx % cols
        row_idx = rows - 1 - (idx // cols)
        
        # Color normalization check
        try:
            if isinstance(color, (tuple, list)):
                norm_color = [c/255.0 for c in color]
            elif isinstance(color, str) and color.startswith('#'):
                norm_color = color
            else:
                norm_color = 'gray'
        except:
            norm_color = 'gray'
            
        rect = patches.Rectangle((col_idx, row_idx), 1, 1, facecolor=norm_color, edgecolor='white')
        ax.add_patch(rect)
        
        # Text label styling
        text_color = 'white' if isinstance(color, (tuple, list)) and sum(color)/3 < 128 else 'black'
        display_name = name[:12] + "..." if len(name) > 12 else name
        
        ax.text(col_idx + 0.5, row_idx + 0.5, f"{idx+1}\n{display_name}", 
                ha='center', va='center', fontsize=10, color=text_color, fontweight='bold')

    ax.axis('off')
    plt.tight_layout()
    plt.show()

# Note: This script requires 'filenames' (list) and 'dominant_colours' (list of RGB tuples) 
# to be defined from the data extraction step.
