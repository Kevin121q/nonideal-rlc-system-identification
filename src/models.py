"""
Physical models for the non-ideal RLC system-identification project.
"""

import numpy as np


def nonideal_rlc_gain(frequency_hz, resistance_measured, resistance_hidden, inductance_h, capacitance_f):
    """
    Gain magnitude for a non-ideal series RLC circuit measured across the resistor.

    Parameters
    ----------
    frequency_hz : array-like
        Frequency in Hz.
    resistance_measured : float
        Measured/load resistor in ohms.
    resistance_hidden : float
        Hidden/effective series resistance in ohms.
    inductance_h : float
        Effective inductance in henries.
    capacitance_f : float
        Effective capacitance in farads.

    Returns
    -------
    gain : array-like
        Predicted gain |VR/Vs|.
    """
    omega = 2 * np.pi * frequency_hz
    resistance_total = resistance_measured + resistance_hidden

    reactance = omega * inductance_h - 1 / (omega * capacitance_f)

    return resistance_measured / np.sqrt(
        resistance_total**2 + reactance**2
    )


def resonance_frequency(inductance_h, capacitance_f):
    """
    Ideal resonance frequency for an LC pair.
    """
    return 1 / (2 * np.pi * np.sqrt(inductance_h * capacitance_f))