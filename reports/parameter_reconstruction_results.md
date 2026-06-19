# Parameter Reconstruction Results

## Objective

The goal of this analysis was to determine whether hidden parameters of a non-ideal RLC circuit could be reconstructed from measured frequency-response data.

A non-ideal transfer-function model was fitted independently to each resistance-sweep dataset. The fitting procedure estimated three effective parameters:

* Hidden resistance, (R_{hidden})
* Effective inductance, (L_{eff})
* Effective capacitance, (C_{eff})

Model quality was evaluated using residual analysis and root-mean-square error (RMSE).

---

## Reconstruction Method

For each measured resistance condition, the experimental gain curve was fitted using a non-ideal series RLC model.

The total damping resistance was modeled as:

R_total = R_measured + R_hidden

The fitting algorithm searched for parameter values that minimized the difference between measured and predicted gain.

For each experiment, the following quantities were recorded:

* Best-fit hidden resistance
* Best-fit effective inductance
* Best-fit effective capacitance
* Reconstructed resonance frequency
* RMSE

---

## Reconstruction Performance

The fitted model successfully reproduced the measured gain curves across all resistance conditions.

Residual errors remained small, indicating that the non-ideal model captured the dominant features of the measured frequency responses.

Representative reconstruction results include:

| Measured Resistance | R_hidden |      L_eff |    C_eff |
| ------------------: | -------: | ---------: | -------: |
|                22 Ω | ≈ 34.5 Ω | ≈ 10.69 mH | ≈ 242 nF |
|               150 Ω |   ≈ 62 Ω | ≈ 12.86 mH | ≈ 201 nF |
|               470 Ω |   ≈ 34 Ω | ≈ 11.41 mH | ≈ 229 nF |

Figures showing fitted curves, residuals, and reconstructed parameters are available in the reconstruction figure directory.

---

## Observed Parameter Drift

Although the model achieved good fits, the recovered parameters were not constant across resistance conditions.

Several systematic trends were observed:

* Hidden resistance varied significantly between experiments.
* Effective inductance drifted across resistance conditions.
* Effective capacitance also varied.
* Reconstructed resonance frequency remained comparatively stable.

This behavior indicates that multiple parameter combinations can reproduce similar measured responses.

---

## Effective Parameter Interpretation

The recovered parameters should not be interpreted as direct measurements of physical component values.

Instead, they behave as effective parameters that absorb multiple physical effects into a simplified model.

Possible contributors include:

* Source impedance
* Inductor winding resistance
* Capacitor ESR
* Breadboard parasitics
* Frequency-dependent losses
* Measurement uncertainty

As a result, the reconstructed parameters represent the best explanation available within the chosen model structure rather than the true underlying component values.

---

## Conclusions

The parameter reconstruction framework successfully recovered parameter sets capable of reproducing measured frequency-response curves with low error.

However, systematic parameter drift suggests the presence of model mismatch and unmodeled physical effects.

The results demonstrate an important distinction between model fitting and physical parameter identification:

A model can fit experimental data well while still failing to recover unique physical parameter values.

This observation motivates the identifiability analysis presented in the next stage of the project.
