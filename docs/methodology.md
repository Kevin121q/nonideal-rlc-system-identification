# Methodology

## Workflow Overview

The project follows a combined experimental and computational workflow:

1. Collect frequency-response measurements.
2. Validate and clean datasets.
3. Analyze resonance behavior.
4. Fit a non-ideal RLC model.
5. Reconstruct effective parameters.
6. Evaluate reconstruction quality.
7. Analyze practical identifiability.
8. Interpret parameter drift and model mismatch.

---

## Data Collection

Frequency-response measurements were collected for multiple resistance conditions.

For each measurement point:

* Frequency
* Vs
* VR
* Gain

were recorded.

---

## Data Cleaning

The datasets were checked for:

* Missing values
* Formatting issues
* Gain consistency
* Potential outliers

Cleaned datasets were stored separately from the raw measurements.

---

## Parameter Reconstruction

A non-ideal transfer-function model was fitted to each experimental gain curve.

The fitted parameters were:

* R_hidden
* L_eff
* C_eff

Model quality was evaluated using RMSE and residual analysis.

---

## Identifiability Analysis

Practical identifiability was investigated using:

* One-dimensional RMSE sweeps
* Two-dimensional RMSE surfaces
* Threshold-based uncertainty bounds

These analyses were used to determine how uniquely parameters can be recovered from the available measurements.
