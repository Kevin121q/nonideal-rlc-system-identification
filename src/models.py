import numpy as np

def nonideal_rlc_gain(f, R_total, L, C):
    omega = 2 * np.pi * f

    numerator = R_total

    denominator = np.sqrt(
        R_total**2 +
        (omega * L - 1/(omega * C))**2
    )

    return numerator / denominator
