"""
Generate basic resistance sweep figures.

Usage:
    python scripts/generate_figures.py
"""

from pathlib import Path

import pandas as pd

from src.plotting import save_gain_curve_plot, save_line_plot


DATA_PATH = Path("data/processed/resistance_sweep_clean.csv")
SUMMARY_PATH = Path("data/processed/resistance_sweep_summary.csv")

FIG_DIR = Path("figures/script_generated")


def main():
    df = pd.read_csv(DATA_PATH)

    save_gain_curve_plot(
        grouped_data=df.groupby("Resistance_Ohm"),
        output_path=FIG_DIR / "gain_curves_all_resistances.png",
        title="Frequency Response Under Varying Resistive Damping",
    )

    if SUMMARY_PATH.exists():
        summary = pd.read_csv(SUMMARY_PATH)

        save_line_plot(
            summary["Resistance_Ohm"],
            summary["Peak_Gain"],
            "Measured Resistance R (Ω)",
            "Peak Gain",
            "Peak Gain vs Resistance",
            FIG_DIR / "peak_gain_vs_resistance.png",
        )

        save_line_plot(
            summary["Resistance_Ohm"],
            summary["Peak_Frequency_Hz"],
            "Measured Resistance R (Ω)",
            "Peak Frequency (Hz)",
            "Peak Frequency vs Resistance",
            FIG_DIR / "peak_frequency_vs_resistance.png",
        )

    print(f"Saved figures to {FIG_DIR}")


if __name__ == "__main__":
    main()