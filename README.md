# Non-Ideal RLC System Identification

Experimental and computational investigation of parameter reconstruction, identifiability, and model mismatch in a non-ideal series RLC circuit.

---

## Overview

This project studies how hidden parameters and non-ideal behavior in a damped RLC circuit can be reconstructed from experimental frequency-response measurements.

A physical series RLC circuit was built and tested using a signal generator and oscilloscope. The measured frequency-response data are analyzed using Python to compare ideal and non-ideal models, estimate effective circuit parameters, study damping and source-loading effects, and investigate when parameter reconstruction becomes ambiguous.

The project focuses on the difference between fitting a model well and correctly identifying the physical parameters of the system. A low fitting error does not automatically mean that the recovered parameters are physically true; it only means that the model reproduces the measured response well. This distinction is central to the project.

---

## Research Question

How accurately can hidden parameters of a non-ideal RLC circuit be reconstructed from frequency-response magnitude data, and when does reconstruction become ambiguous due to damping, source loading, parameter correlation, and model mismatch?

---

## Experimental System

The circuit topology is:

```text
Signal generator → Inductor → Capacitor → Resistor → Ground
```

The measured output is the voltage across the resistor.

Measured quantities:

* Frequency
* Source voltage `Vs`
* Resistor voltage `VR`
* Gain, calculated as `Gain = VR / Vs`

Equipment:

* FY6900 signal generator
* FNIRSI 5012H oscilloscope
* Breadboard
* Resistors
* Inductor
* Polyester capacitor

---

## Methodology

The project follows a complete experimental and computational workflow:

1. Collect frequency-response measurements across multiple resistance conditions.
2. Clean and validate the experimental data.
3. Plot resonance curves and source-loading behavior.
4. Fit a non-ideal RLC transfer-function model to the measured gain curves.
5. Estimate effective hidden resistance, inductance, and capacitance.
6. Evaluate reconstruction quality using residuals and RMSE.
7. Analyze practical identifiability using one-dimensional and two-dimensional RMSE landscapes.
8. Interpret parameter drift as evidence of model mismatch and effective-parameter behavior.

---

## Non-Ideal RLC Model

The model treats the total damping resistance as:

```text
R_total = R_measured + R_hidden
```

The fitted parameters are:

* `R_hidden`
* `L_eff`
* `C_eff`

These are interpreted as effective parameters, not guaranteed direct physical measurements of individual components.

---

## Results

### Experimental Results

The resistance sweep shows that damping strongly changes the measured frequency response.

Observed behavior:

* Peak gain increases with measured resistance.
* Low-resistance configurations show stronger source-loading effects.
* High-resistance curves become flatter and less sharply resonant.
* Resonance frequency remains comparatively stable while gain and bandwidth change significantly.
* Ideal RLC assumptions are insufficient because the measured source voltage is not constant.

### Parameter Reconstruction

A non-ideal RLC model was fitted to experimental gain curves. For each resistance condition, the fitting process estimated:

* hidden resistance
* effective inductance
* effective capacitance
* reconstructed resonance frequency
* RMSE

Example reconstructed parameters:

| Measured Resistance | R_hidden |      L_eff |    C_eff |
| ------------------: | -------: | ---------: | -------: |
|                22 Ω | ≈ 34.5 Ω | ≈ 10.69 mH | ≈ 242 nF |
|               150 Ω |   ≈ 62 Ω | ≈ 12.86 mH | ≈ 201 nF |
|               470 Ω | ≈ 35.4 Ω | ≈ 11.41 mH | ≈ 229 nF |

The model fits the measured curves well, but the recovered parameters drift systematically across resistance conditions.

### Identifiability Analysis

Practical identifiability was studied using RMSE sweeps and RMSE maps.

Completed analyses include:

* 1D RMSE sweeps for `R_hidden`, `L_eff`, and `C_eff`
* 2D RMSE maps for `L_eff-C_eff`
* 2D RMSE maps for `R_hidden-L_eff`
* 2D RMSE maps for `R_hidden-C_eff`
* 5% and 10% RMSE-threshold uncertainty intervals

Key findings:

* Parameters are practically identifiable within individual experiments.
* Uncertainty intervals are relatively small.
* The product `L_eff × C_eff` remains nearly constant.
* Reconstructed resonance frequency remains within approximately 2% of its mean value.
* `L_eff` and `C_eff` show a strong tradeoff relationship.
* Hidden resistance likely compensates for unmodeled physical effects.

---

## Scientific Interpretation

The parameter drift is likely caused by model mismatch.

The simplified model combines several physical effects into a small number of effective parameters. Possible unmodeled effects include:

* source impedance
* inductor winding resistance
* capacitor ESR
* breadboard parasitics
* frequency-dependent losses
* measurement limitations

Therefore, the reconstructed values should be interpreted as effective model parameters rather than direct measurements of the true physical component values. This distinction motivates the use of identifiability analysis, since accurate curve fitting alone is insufficient evidence that a parameter estimate corresponds uniquely to the underlying physical system.

---

## Repository Structure

```text
data/
├── raw/                  Original experimental measurements
├── cleaned/              Validated and standardized datasets
└── processed/            Summary tables and reconstruction outputs

figures/
├── experimental/         Resistance sweeps, source loading, repeatability
├── reconstruction/       Fitted curves, residuals, parameter drift
└── identifiability/      RMSE sweeps, RMSE maps, uncertainty bounds

notebooks/                Exploratory and reproducible analyses
reports/                  Written technical summaries
src/                      Reusable Python modules
scripts/                  Executable analysis scripts
docs/                     Experimental setup, theory, and methodology
```

---

## Current Status

Completed:

* Experimental series RLC circuit construction
* Frequency-response measurements
* Multiple resistance sweep datasets
* Data cleaning
* Repeatability analysis
* Source-loading analysis
* Non-ideal model fitting
* Parameter reconstruction
* Residual and RMSE analysis
* Practical identifiability analysis
* Uncertainty interval estimation

In progress:

* Improved model interpretation
* Sensitivity analysis
* Source impedance modeling
* More detailed uncertainty quantification

---

## Future Work

Planned extensions:

* Sensitivity analysis
* Parameter correlation analysis
* Monte Carlo uncertainty propagation
* Source impedance modeling
* Capacitor ESR modeling
* Inductor winding resistance modeling
* Structural identifiability analysis
* Practical identifiability under noise
* Improved non-ideal transfer-function models

---

## Educational Value

This repository is intended to serve as:

- a reproducible experimental RLC dataset,
- an example of system-identification workflows,
- an introduction to practical identifiability analysis,
- a resource for students interested in modeling real-world dynamical systems.

All data, figures, and analysis workflows are provided openly to encourage reproducibility and further exploration.

## License

This project is released under the MIT License.
