# Resistance Sweep Experiment

## Objective

The purpose of this experiment was to investigate how resistive damping influences the measured frequency response of a real series RLC circuit.

By collecting frequency-response measurements across multiple resistor values, the experiment explores:

- resonance behavior
- damping effects
- source loading
- information content available for parameter reconstruction

The resistance sweep serves as a foundation for later system-identification and parameter-estimation analyses.

## Experimental Method

A series RLC circuit was assembled using a signal generator, inductor, capacitor, and interchangeable resistors.

For each resistance value, the excitation frequency was swept across the resonance region.

The following quantities were recorded:

- Frequency
- Source voltage (Vs)
- Resistor voltage (VR)

Gain was computed as:

Gain = VR / Vs

Measurements were repeated across resistor values ranging from 22 Ω to 470 Ω.

## Dataset

Resistances investigated:

22 Ω
47 Ω
100 Ω
150 Ω
200 Ω
270 Ω
330 Ω
470 Ω

Frequency range:

1000 Hz – 5000 Hz

Measurement outputs:

- Frequency
- Vs
- VR
- Gain

 ![Resistance Sweep](figures/resistance_sweep1/resistance_sweep_gain_curves1.png)

 ## Key Observations

1. Peak gain increased systematically with resistance.

2. Low-resistance configurations exhibited stronger source-loading effects, producing larger reductions in measured source voltage near resonance.

3. Increasing resistance broadened the resonance response and reduced the distinctiveness of resonance features.

4. The resonance frequency remained relatively stable across the resistance sweep despite substantial changes in gain and bandwidth.

5. The measured behavior cannot be fully explained by ideal RLC models that assume a constant source voltage.

## Limitations

Several limitations affect interpretation of the results:

- Source voltage was not perfectly constant across frequency.
- Measurement resolution limits bandwidth estimation accuracy.
- Half-power bandwidth calculations are approximate and based on discrete sampling points.
- Component tolerances and parasitic resistances were not independently measured.
- The circuit was implemented on a breadboard, introducing additional non-ideal effects.

## Conclusions

The resistance sweep demonstrates that damping strongly influences the information available in frequency-response measurements.

Although resonance frequency remains relatively stable, gain, bandwidth, and source-loading effects change substantially with resistance.

These observations suggest that parameter reconstruction accuracy depends not only on component values but also on the amount of information preserved in the measured response.

The experiment provides a foundation for future system-identification analyses aimed at reconstructing hidden circuit parameters from experimental data.

## Next Steps

Planned analyses include:

- non-ideal model development
- hidden resistance estimation
- parameter reconstruction
- residual analysis
- uncertainty quantification
- identifiability analysis
