# Cleaned Data

This folder will contain validated versions of the raw datasets.

Cleaning steps may include:

- sorting by resistance and frequency
- checking that `Gain = VR_Vpp / Vs_Vpp`
- flagging suspicious values
- standardizing column names
- preserving all original measurements unless a clear error is documented

Cleaned data should be generated from files in `data/raw/` using reproducible Python scripts.
