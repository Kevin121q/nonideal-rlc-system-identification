# Non-Ideal RLC System Identification

Experimental and computational analysis of a non-ideal series RLC circuit using frequency-response measurements, parameter estimation, and system-identification techniques.

---

## Overview

This project investigates how accurately hidden parameters and non-ideal behavior in a damped RLC circuit can be reconstructed from experimental frequency-response measurements.

A physical series RLC circuit was built and measured using a signal generator and oscilloscope. The resulting datasets are analyzed using Python to compare ideal and non-ideal models, study damping effects, quantify source loading, and explore the limits of parameter reconstruction.

---

## Research Questions

- How does damping affect resonance behavior?
- How strongly does source loading distort measurements?
- Which circuit parameters can be reconstructed reliably?
- When does reconstruction become ambiguous?

---

## Experimental Setup

Circuit:

Generator → L → C → R → Ground

Measured quantity:

Gain = VR / Vs

Equipment:

- FY6900 Signal Generator
- FNIRSI 5012H Oscilloscope
- Breadboard
- Resistors
- Inductor
- Polyester Capacitor

---

## Current Progress

Completed:

- Baseline R = 100Ω dataset
- Multi-resistance sweep dataset
- Gain analysis
- Resonance analysis
- Bandwidth and Q-factor analysis
- Source-loading investigation

In Progress:

- Hidden resistance estimation
- Non-ideal model fitting
- Parameter reconstruction
- Identifiability analysis

---

## Repository Structure

(To be completed)

---

## Results

(To be completed)

---

## Future Work

- Non-ideal parameter estimation
- Reconstruction error analysis
- Identifiability studies
- Educational notebooks
