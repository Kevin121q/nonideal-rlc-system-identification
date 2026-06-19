# Identifiability Analysis Results

## Objective

The purpose of this analysis was to determine whether the reconstructed parameters are uniquely determined by the experimental measurements.

Even when a model fits data well, multiple parameter combinations may produce nearly identical responses. This phenomenon is known as practical non-identifiability.

The analysis investigates how sensitive reconstruction quality is to variations in hidden resistance, inductance, and capacitance.

---

## Methodology

Practical identifiability was evaluated using RMSE landscapes generated around the best-fit parameter values.

The following analyses were performed:

### One-Dimensional RMSE Sweeps

Parameters were varied individually while holding the remaining parameters fixed.

Sweeps were generated for:

* Hidden resistance
* Effective inductance
* Effective capacitance

### Two-Dimensional RMSE Maps

Parameter pairs were varied simultaneously.

Maps were generated for:

* L_eff – C_eff
* R_hidden – L_eff
* R_hidden – C_eff

### Uncertainty Bounds

Parameter uncertainty intervals were estimated using:

* 5% RMSE threshold
* 10% RMSE threshold

relative to the minimum observed RMSE.

---

## Results

The RMSE landscapes exhibit clear minima near the reconstructed parameter values.

This indicates that the measured data contain sufficient information to constrain the parameter estimates.

Key observations include:

* Practical uncertainty intervals are relatively small.
* Individual experiments produce well-defined parameter estimates.
* Parameter reconstruction is stable within local neighborhoods of the optimum.
* Significant deviations from the optimum produce noticeable increases in RMSE.

---

## Parameter Correlations

Although parameters are locally identifiable, strong correlations are present.

The most significant relationship appears between effective inductance and effective capacitance.

The L_eff–C_eff RMSE maps reveal elongated low-error regions, indicating a tradeoff between these parameters.

Increasing one parameter can often be partially compensated by decreasing the other while maintaining a similar resonance response.

This behavior is consistent with the dependence of resonance frequency on the product LC.

---

## Resonance Stability

Despite variations in reconstructed parameters, the reconstructed resonance frequency remains remarkably stable.

Across all resistance conditions, resonance frequency varies by only a small percentage.

This suggests that the fitting process primarily preserves resonance behavior while redistributing uncertainty among the individual parameter estimates.

---

## Implications for Model Interpretation

The identifiability analysis demonstrates that the reconstruction problem is not completely ambiguous.

Parameters are practically identifiable within individual experiments.

However, the observed parameter correlations indicate that the reconstructed values should be interpreted cautiously.

Small uncertainty intervals do not necessarily imply that the recovered parameters correspond directly to physical component values.

Instead, they represent the most likely effective parameters within the assumptions of the chosen model.

---

## Conclusions

The identifiability analysis shows that:

* The reconstruction problem is locally well-conditioned.
* Practical uncertainty intervals are relatively small.
* Strong parameter correlations exist.
* L_eff and C_eff exhibit a clear tradeoff relationship.
* Resonance frequency remains significantly more stable than individual parameter values.

These results support the interpretation that systematic parameter drift is primarily caused by model mismatch rather than measurement noise alone.

Future work will investigate more detailed non-ideal circuit models and advanced inverse-problem techniques to separate physical effects from effective parameter behavior.
