"""
Run per-resistance parameter reconstruction.

Usage:
    python scripts/run_reconstruction.py
"""

from pathlib import Path

import pandas as pd

from src.fitting import fit_single_resistance_curve


DATA_PATH = Path("data/processed/resistance_sweep_clean.csv")
OUT_PATH = Path("data/processed/parameter_reconstruction_script_output.csv")


def main():
    df = pd.read_csv(DATA_PATH)

    results = []

    for resistance, group in df.groupby("Resistance_Ohm"):
        result = fit_single_resistance_curve(
            frequency_hz=group["Frequency_Hz"].values,
            gain=group["Gain"].values,
            resistance_measured=resistance,
        )

        result.pop("Covariance", None)
        results.append(result)

    results_df = pd.DataFrame(results)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    results_df.to_csv(OUT_PATH, index=False)

    print(f"Saved reconstruction results to {OUT_PATH}")


if __name__ == "__main__":
    main()