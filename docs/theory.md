# Theory

## Ideal Series RLC Circuit

A series RLC circuit consists of:

* Resistance (R)
* Inductance (L)
* Capacitance (C)

When driven by a sinusoidal source, the circuit exhibits resonance at a characteristic frequency determined by the inductance and capacitance.

Approximate resonance frequency:

f₀ = 1 / (2π√(LC))

At resonance, the inductive and capacitive reactances cancel, producing a distinct peak in the frequency response.

---

## Damping

Resistance controls the damping of the system.

Increasing resistance:

* Reduces resonance sharpness
* Broadens the frequency response
* Lowers the quality factor
* Reduces information available for parameter reconstruction

Damping therefore influences both the physical behavior of the circuit and the difficulty of the inverse problem.

---

## Source Loading

Textbook models typically assume an ideal voltage source with constant amplitude.

In practice, the signal generator interacts with the circuit.

As load conditions change, the measured source voltage may vary with frequency.

This source-loading effect introduces non-ideal behavior that is not captured by simple ideal RLC models.

---

## Effective Parameters

The fitted parameters used in this project are interpreted as effective parameters.

These parameters do not necessarily correspond directly to physical component values.

Instead, they represent the values required for a simplified model to reproduce the measured behavior.

Effective parameters may absorb:

* Source impedance
* Inductor winding resistance
* Capacitor ESR
* Breadboard parasitics
* Frequency-dependent losses

---

## Model Mismatch

Model mismatch occurs when the mathematical model does not fully represent the underlying physical system.

A model may reproduce measured data accurately while still failing to recover the true physical parameters.

Understanding this distinction is one of the central motivations of the project.
