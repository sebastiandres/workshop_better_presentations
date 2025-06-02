# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

import os
from matplotlib.lines import Line2D

FONT_SIZE = 18

def create_figure(df):
    # number of variable
    categories=list(df)[1:]
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    fig = plt.figure(figsize=(16,9))
    ax = plt.subplot(111, polar=True)

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels
    plt.xticks(angles[:-1], categories, fontsize=FONT_SIZE, color='grey')

    # Draw ylabels
    ax.set_rlabel_position(0)
    yticks = [2, 4, 6, 8]
    plt.yticks(yticks, [str(i) for i in yticks], color="grey", size=FONT_SIZE)
    plt.ylim(0,10)

    return ax, angles

def add_values_to_plot(ax, n, angles, all_values, color, name):
    for i in range(n):
        if i==(n-1):
            c = color
        else:
            c = 'grey'
        _, values = all_values[i,0], all_values[i,1:].tolist()
        values += values[:1] # close the plot
        ax.plot(angles, values, c, linewidth=1, linestyle='solid', label=name)
        if i==(n-1):
            ax.fill(angles, values, c, alpha=0.1)

    if n>0:
        # Add legend
        custom_lines = [Line2D([0], [0], color=color, lw=1)]
        # Position outside the plot so it won't overlap with the data
        ax.legend(custom_lines, [name], fontsize=FONT_SIZE,
                bbox_to_anchor=(1.05, 1), loc='upper left')

    # Show the graph
    name_clean = name.split(",")[0].replace(" ", "_")
    filename = f"{n}_{name_clean}.png"
    filepath = os.path.join(os.path.dirname(__file__), filename)
    # Save in high resolution
    plt.savefig(filepath, dpi=300)
    plt.close()
    return

def create_radar_plot(df, n, color, name):
    # Create figure
    ax, angles = create_figure(df)
    all_values = df.values
    # Add values to plot
    add_values_to_plot(ax, n, angles, all_values, color, name)

if __name__=="__main__":
    filepath = os.path.join(os.path.dirname(__file__), "strengths_sebastian_flores.xlsx")
    df = pd.read_excel(filepath)
    create_radar_plot(df, 0, 'k', name="baseline")
    create_radar_plot(df, 1, 'k', name="UTFSM, Chile")
    create_radar_plot(df, 2, 'b', name="École Polytechnique,\nFrancia")
    create_radar_plot(df, 3, 'r', name="Stanford, USA")
    create_radar_plot(df, 4, 'g', name="Work")

