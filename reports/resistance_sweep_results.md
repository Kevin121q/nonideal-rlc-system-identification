# Resistance Sweep Results

## Objective

The objective of this experiment was to investigate how resistive damping influences the measured frequency response of a non-ideal series RLC circuit.

By systematically varying the resistance and measuring the resulting frequency-response curves, the experiment explores how damping affects resonance behavior, source loading, information content, and the feasibility of parameter reconstruction.

These measurements provide the experimental foundation for all subsequent model-fitting and identifiability analyses.

---

## Experimental Method

A series RLC circuit was constructed using a signal generator, inductor, capacitor, and interchangeable resistors.

For each resistance condition, the excitation frequency was swept across the resonance region while the following quantities were recorded:

* Frequency
* Source voltage, (V_S)
* Resistor voltage, (V_R)

The measured gain was calculated as:

[
\text{Gain} = \frac{V_R}{V_S}
]

Measurements were performed for resistor values ranging from 22 Ω to 470 Ω.

The frequency range was selected to fully capture the resonance peak and surrounding response behavior.

---

## Experimental Results

The measured gain curves reveal a strong dependence on resistive damping.

As resistance increases:

* Peak gain increases.
* Resonance curves broaden.
* Frequency-response behavior becomes less sharply defined.
* Source-loading effects become less severe.

The measured source voltage was found to vary significantly with frequency, particularly for low-resistance configurations.

This behavior demonstrates that the experimental system cannot be accurately described using an ideal voltage source assumption.

---

## Source Loading

One of the most significant observations is the frequency dependence of the measured source voltage.

For low resistance values, the source voltage decreases substantially near resonance.

This effect becomes progressively weaker as resistance increases.

The source-loading measurements indicate that the signal generator interacts with the circuit rather than behaving as an ideal voltage source.

As a result, models that assume constant excitation amplitude cannot fully explain the observed behavior.

---

## Resonance Characteristics

Approximate resonance frequencies remained relatively stable across the resistance sweep.

In contrast, gain and bandwidth changed substantially.

This suggests that damping primarily affects the sharpness and amplitude of the resonance response rather than the underlying resonant frequency itself.

The measured Q-factor decreases systematically as resistance increases, indicating progressive loss of resonance selectivity.

---

## Implications for Parameter Reconstruction

The resistance sweep demonstrates that the information available for parameter reconstruction depends strongly on damping.

Low-damping conditions produce narrow and highly distinctive resonance curves.

High-damping conditions produce broader responses that contain less uniquely identifiable information.

Consequently, reconstruction accuracy is expected to depend not only on measurement quality but also on the amount of information preserved in the measured response.

---

## Limitations

Several limitations affect interpretation of the results:

* Source voltage is not constant across frequency.
* Bandwidth estimates are based on discrete frequency samples.
* Component tolerances were not independently characterized.
* Parasitic resistances and losses were not directly measured.
* Breadboard construction introduces additional non-ideal effects.
* Measurement uncertainty is not explicitly incorporated into the current analysis.

---

## Conclusions

The resistance sweep reveals that damping significantly influences the observable behavior of the system.

Although resonance frequency remains comparatively stable, gain, bandwidth, Q-factor, and source-loading effects vary substantially across resistance conditions.

These observations demonstrate that accurate parameter reconstruction requires accounting for non-ideal effects beyond those included in ideal textbook RLC models.

The results motivate the development of non-ideal models capable of explaining both the measured frequency response and the observed parameter drift identified in later analyses.
