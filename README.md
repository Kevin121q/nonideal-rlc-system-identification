# Non-Ideal RLC System Identification

Experimental and computational analysis of a non-ideal series RLC circuit using frequency-response measurements, parameter estimation, and system-identification techniques.

---

## Overview

This project investigates how accurately hidden parameters and non-ideal behavior in a damped RLC circuit can be reconstructed from experimental frequency-response measurements.

A physical series RLC circuit was built and tested using a signal generator and oscilloscope. Experimental measurements were analyzed using Python to compare ideal and non-ideal models, study damping effects, investigate source loading, and explore the limits of parameter reconstruction.

---

## Motivation

Textbook RLC circuits are typically modeled as ideal systems. Real circuits contain non-ideal effects such as parasitic resistance, source loading, component tolerances, and measurement limitations.

The goal of this project is not only to model resonance behavior, but also to understand when hidden circuit parameters can and cannot be reconstructed from experimental data.

---

## Research Questions

- How does damping affect frequency-response measurements?
- How strongly does source loading influence observed gain?
- Which circuit parameters can be reconstructed reliably?
- When does parameter estimation become ambiguous?
- How much information is lost as damping increases?

---

## Experimental Setup

Circuit topology:

Generator → Inductor → Capacitor → Resistor → Ground

Measured quantities:

- Frequency
- Source voltage (Vs)
- Resistor voltage (VR)

Gain calculation:

Gain = VR / Vs

Equipment:

- FY6900 Signal Generator
- FNIRSI 5012H Oscilloscope
- Breadboard
- Resistors
- Inductor
- Polyester Capacitor

---

## Datasets

Current datasets include:

### Baseline Dataset

Frequency-response measurements for a 100 Ω resistor.

### Resistance Sweep Dataset

Frequency-response measurements collected across multiple resistor values:

22 Ω, 47 Ω, 100 Ω, 150 Ω, 200 Ω, 270 Ω, 330 Ω, 470 Ω

Used to study:

- damping
- resonance broadening
- source loading
- information content
- parameter reconstructability

---

## Current Results

Key observations:

- Peak gain increases with resistance.
- Low-resistance circuits exhibit stronger source-loading effects.
- High-resistance circuits produce flatter resonance curves.
- Damping changes the amount of information available for parameter reconstruction.
- Ideal models alone are insufficient to explain all measured behavior.

---

## Repository Structure

(To be completed)

---

## Future Work

Planned analyses:

- Non-ideal parameter estimation
- Hidden resistance reconstruction
- Model fitting and residual analysis
- Reconstruction error quantification
- Identifiability analysis
- Educational notebooks and reproducible workflows

---

## License

MIT License
