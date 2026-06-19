# Identifiability and Uncertainty Figures

This folder investigates parameter identifiability, parameter coupling, and uncertainty in the reconstruction process.

The central question is:

Can model parameters be uniquely recovered from frequency-response measurements, or do multiple parameter combinations produce nearly identical fits?

---

## RMSE 1D Analysis

### R_hidden_identifiability_R_*.png

One-dimensional RMSE scans showing sensitivity of model error to hidden resistance values.

### L_identifiability_R_*.png

One-dimensional RMSE scans for effective inductance.

### C_identifiability_R_*.png

One-dimensional RMSE scans for effective capacitance.

These plots help determine how strongly each parameter is constrained by the available data.

---

## RMSE 2D Analysis

### LC_heatmap_R_*.png

Two-dimensional RMSE landscapes for inductance-capacitance parameter pairs.

### Rhidden_C_heatmap_R_*.png

Two-dimensional RMSE landscapes for hidden-resistance and capacitance parameter pairs.

### Rhidden_L_heatmap_R_*.png

Two-dimensional RMSE landscapes for hidden-resistance and inductance parameter pairs.

These figures reveal parameter tradeoffs and regions of ambiguity where multiple parameter combinations generate similar model responses.

---

## Uncertainty Bounds

### R_hidden_uncertainty_bounds.png

Estimated uncertainty range for hidden resistance reconstruction.

### L_eff_uncertainty_bounds.png

Estimated uncertainty range for effective inductance reconstruction.

### C_eff_uncertainty_bounds.png

Estimated uncertainty range for effective capacitance reconstruction.

### parameter_uncertainty_vs_resistance.png

Comparison of reconstruction uncertainty across different resistance values.
