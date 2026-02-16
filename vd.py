import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_hickory_venn_diagram():

    fig, ax = plt.subplots(figsize=(10, 10))

    fig.patch.set_facecolor('#F0F0F0') 
    ax.set_facecolor('#F0F0F0')

    circle_settings = [
        {'center': (0.35, 0.6), 'radius': 0.35},  # Top Left
        {'center': (0.65, 0.6), 'radius': 0.35},  # Top Right
        {'center': (0.5, 0.35), 'radius': 0.35}   # Bottom
    ]

    for circle in circle_settings:
        c = patches.Circle(
            circle['center'],
            circle['radius'],
            linewidth=6,
            edgecolor='#333333',
            facecolor='none'
        )
        ax.add_patch(c)

    text_elements = [
        (0.20, 0.65, 'K', 'black', 35),
        (0.16, 0.55, 'F', 'black', 15),
        (0.28, 0.50, 'Z', 'blue', 35), 
        (0.24, 0.74, 'E', 'black', 35),

        (0.80, 0.70, 'C', 'black', 65),
        (0.84, 0.60, 'S', 'black', 35),
        (0.75, 0.55, 'Q', 'black', 35),
        (0.71, 0.64, 'U', 'black', 15),

        (0.50, 0.08, 'λ', 'black', 40), 
        (0.40, 0.14, 'β', 'green', 50), 
        (0.60, 0.16, 'δ', 'black', 40), 
        (0.50, 0.20, 'α', 'purple', 40), 

        (0.50, 0.75, 'D', 'black', 67),
        (0.40, 0.695, 'T', 'black', 10),
        (0.42, 0.77, 'Q', 'black', 10),
        (0.44, 0.67, 'K', 'black', 10),
        (0.47, 0.65, 'P', 'red', 35), 
        (0.53, 0.58, 'G', 'black', 35),

        (0.31, 0.40, 'Δ', 'black', 40), 
        (0.38, 0.28, 'Σ', 'yellow', 40), 
        (0.26, 0.31, 'Ξ', 'black', 40),

        (0.69, 0.41, 'Ω', 'black', 40), 
        (0.62, 0.28, 'θ', 'red', 46), 
        (0.78, 0.35, 'ε', 'black', 60),

        (0.50, 0.45, '?', 'darkgreen', 50)
    ]

    for x, y, char, color, size in text_elements:
        ax.text(
            x, y, char,
            color=color,
            fontsize=size,
            ha='center',
            va='center',
            fontfamily='serif',
            fontweight='bold'
        )

    # 4. Final Formatting
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # 5. Save/Show
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    create_hickory_venn_diagram()
