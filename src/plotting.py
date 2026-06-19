"""
Plotting utilities for RLC analysis figures.
"""

from pathlib import Path

import matplotlib.pyplot as plt


def save_line_plot(x, y, xlabel, ylabel, title, output_path):
    """
    Save a simple publication-quality line plot.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(x, y, "o-", linewidth=2)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True, alpha=0.35)

    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def save_gain_curve_plot(grouped_data, output_path, title):
    """
    Save gain curves grouped by resistance.

    grouped_data should be an iterable of:
    (resistance, dataframe)
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 6))

    for resistance, group in grouped_data:
        ax.semilogx(
            group["Frequency_Hz"],
            group["Gain"],
            "o-",
            linewidth=2,
            markersize=4,
            label=f"{resistance:.0f} Ω",
        )

    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Gain |VR/Vs|")
    ax.set_title(title)
    ax.grid(True, which="both", alpha=0.35)
    ax.legend(title="Resistance")

    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)