"""
Clean raw resistance sweep data and recompute gain.

Usage:
    python scripts/clean_data.py
"""

from pathlib import Path

import pandas as pd


RAW_PATH = Path("data/raw/resistance_sweep_dataset.csv")
OUT_PATH = Path("data/processed/resistance_sweep_clean.csv")


def main():
    df = pd.read_csv(RAW_PATH)
    df.columns = df.columns.str.strip()

    df = df.rename(columns={
        "R": "Resistance_Ohm",
        "Resistance": "Resistance_Ohm",
        "Frequency": "Frequency_Hz",
        "Vs": "Vs_Vpp",
        "VR": "VR_Vpp",
        "Vr": "VR_Vpp",
    })

    required = ["Resistance_Ohm", "Frequency_Hz", "Vs_Vpp", "VR_Vpp"]

    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    for col in required:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=required)

    df["Gain"] = df["VR_Vpp"] / df["Vs_Vpp"]

    df = df.sort_values(["Resistance_Ohm", "Frequency_Hz"]).reset_index(drop=True)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)

    print(f"Saved cleaned data to {OUT_PATH}")


if __name__ == "__main__":
    main()