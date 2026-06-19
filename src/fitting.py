"""
Fitting utilities for RLC parameter reconstruction.
"""

import numpy as np
from scipy.optimize import curve_fit

from src.models import nonideal_rlc_gain, resonance_frequency


def rmse(y_true, y_pred):
    """
    Root mean square error.
    """
    return np.sqrt(np.mean((y_true - y_pred) ** 2))


def fit_single_resistance_curve(
    frequency_hz,
    gain,
    resistance_measured,
    initial_guess=(40, 10e-3, 220e-9),
    bounds=(
        (0, 5e-3, 100e-9),
        (200, 20e-3, 400e-9),
    ),
):
    """
    Fit one measured resistance sweep.

    Fitted parameters:
    - hidden resistance
    - effective inductance
    - effective capacitance
    """

    def model_for_fit(f, resistance_hidden, inductance_h, capacitance_f):
        return nonideal_rlc_gain(
            f,
            resistance_measured,
            resistance_hidden,
            inductance_h,
            capacitance_f,
        )

    params, covariance = curve_fit(
        model_for_fit,
        frequency_hz,
        gain,
        p0=initial_guess,
        bounds=bounds,
        maxfev=50000,
    )

    resistance_hidden, inductance_h, capacitance_f = params
    fitted_gain = model_for_fit(frequency_hz, *params)

    return {
        "Resistance": resistance_measured,
        "R_hidden_Ohm": resistance_hidden,
        "L_H": inductance_h,
        "L_mH": inductance_h * 1e3,
        "C_F": capacitance_f,
        "C_nF": capacitance_f * 1e9,
        "f0_Hz": resonance_frequency(inductance_h, capacitance_f),
        "RMSE": rmse(gain, fitted_gain),
        "Covariance": covariance,
    }