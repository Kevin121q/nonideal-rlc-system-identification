# Parameter Reconstruction Figures

This folder contains figures related to parameter estimation and reconstruction of the non-ideal RLC model from experimental frequency-response measurements.

## Fitted Curves

### fit_vs_data_R_*.png

Comparison between measured frequency-response data and the fitted non-ideal model for each resistance value.

These figures evaluate how accurately the model reproduces the observed experimental behavior.

---

## Residual Analysis

### residuals_R_*.png

Residual errors between measured data and fitted model predictions.

Residual plots are used to identify systematic deviations, model limitations, and potential experimental artifacts.

---

## Parameter Trends

### R_hidden_vs_measured_R_with_uncertainty.png

Estimated hidden resistance as a function of measured resistance, including uncertainty bounds.

### L_eff_vs_measured_R_with_uncertainty.png

Estimated effective inductance across resistance values.

### C_eff_vs_measured_R_with_uncertainty.png

Estimated effective capacitance across resistance values.

### reconstructed_f0_vs_measured_R.png

Reconstructed resonance frequency obtained from fitted parameters.

### RMSE_vs_measured_R.png

Root-mean-square fitting error for each reconstructed model.

### LC_tradeoff_scatter.png

Relationship between reconstructed inductance and capacitance estimates.

### run_comparison_R_hidden.png

### run_comparison_L_eff.png

### run_comparison_C_eff.png

Comparison of reconstructed parameters between independent experimental runs, providing an assessment of reconstruction stability and repeatability.
