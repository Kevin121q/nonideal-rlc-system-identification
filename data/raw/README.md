# Raw Data

This folder contains original experimental measurements.

## resistance_sweep_dataset.csv

Frequency-response measurements for a series RLC circuit across multiple resistor values.

Columns:

- `Resistance_Ohm`: measured resistor value used in the circuit
- `Frequency_Hz`: input signal frequency
- `Vs_Vpp`: measured source voltage peak-to-peak
- `VR_Vpp`: measured resistor voltage peak-to-peak
- `Gain`: voltage gain, calculated as `VR_Vpp / Vs_Vpp`

The dataset includes multiple damping regimes, from low resistance to high resistance. It is used to study resonance behavior, bandwidth, Q-factor, source loading, and future parameter reconstruction.

Raw data should not be manually edited.
