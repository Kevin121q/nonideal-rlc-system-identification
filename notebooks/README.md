# Notebooks

This directory contains the primary Jupyter notebooks used throughout the project.

The notebooks document the complete workflow from experimental data collection to parameter reconstruction and identifiability analysis.

---

## Notebook Overview

### 01_data_cleaning.ipynb

Purpose:

* Import raw experimental measurements
* Validate data integrity
* Standardize column names
* Recompute gain values
* Detect potential outliers
* Generate cleaned datasets

Outputs:

* Cleaned CSV files
* Data quality checks
* Preliminary summaries

---

### 02_resistance_sweep_analysis.ipynb

Purpose:

* Analyze frequency-response measurements across multiple resistance values
* Investigate damping effects
* Quantify resonance behavior
* Study source-loading effects

Outputs:

* Resistance sweep gain curves
* Source-loading plots
* Peak gain trends
* Bandwidth estimates
* Q-factor estimates
* Experimental summary tables

---

### 03_parameter_reconstruction.ipynb

Purpose:

* Fit a non-ideal RLC transfer-function model to experimental measurements
* Estimate effective circuit parameters

Reconstructed parameters:

* Hidden resistance (R_hidden)
* Effective inductance (L_eff)
* Effective capacitance (C_eff)

Outputs:

* Best-fit parameter estimates
* Fitted model curves
* Residual plots
* RMSE calculations
* Parameter drift analysis

---

### 04_identifiability_analysis.ipynb

Purpose:

* Investigate practical identifiability of reconstructed parameters
* Quantify uncertainty and parameter ambiguity

Methods:

* One-dimensional RMSE sweeps
* Two-dimensional RMSE landscapes
* Threshold-based uncertainty bounds

Outputs:

* RMSE maps
* Parameter uncertainty intervals
* Tradeoff analyses
* Identifiability summaries

---

## Reproducibility

The notebooks are intended to provide a transparent and reproducible analysis workflow.

All figures and summary tables contained in the repository should be reproducible from the provided datasets and notebooks.
