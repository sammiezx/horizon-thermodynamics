"""Basic Hawking-radiation formulas for a Schwarzschild black hole.

Units: SI by default. Pass `natural_units=True` to use \\(\\hbar = c = k_B = G = 1\\),
in which case `mass` is interpreted as already-dimensionless.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray

# CODATA 2018 constants (SI)
HBAR = 1.054_571_817e-34       # J*s
C = 2.997_924_58e8             # m/s
K_B = 1.380_649e-23            # J/K
G_N = 6.674_30e-11             # m^3 / (kg * s^2)


def hawking_temperature(mass: float, *, natural_units: bool = False) -> float:
    r"""Hawking temperature of a Schwarzschild black hole of mass `mass`.

    .. math::

        T_H = \frac{\hbar c^3}{8\pi G_N M k_B}

    Parameters
    ----------
    mass
        Black hole mass. Kilograms in SI; dimensionless in natural units.
    natural_units
        If True, use \\(\\hbar = c = k_B = G = 1\\) so that \\(T_H = 1/(8\\pi M)\\).

    Returns
    -------
    Temperature in kelvin (SI) or in natural units.
    """
    if mass <= 0:
        raise ValueError(f"mass must be positive, got {mass}")
    if natural_units:
        return 1.0 / (8.0 * np.pi * mass)
    return (HBAR * C**3) / (8.0 * np.pi * G_N * mass * K_B)


def planck_spectrum(
    frequency: ArrayLike,
    temperature: float,
    *,
    natural_units: bool = False,
) -> NDArray[np.float64]:
    r"""Planck (thermal) spectral energy density at angular frequency `frequency`.

    This is the *thermal* spectrum a distant observer would see if greybody factors
    were unity. To get the physical Hawking spectrum, multiply by the
    frequency-dependent greybody factor \\(\\Gamma_{\\ell}(\\omega)\\).

    .. math::

        u(\omega) = \frac{\hbar \omega^3}{\pi^2 c^3}
                    \frac{1}{\exp(\hbar \omega / k_B T) - 1}

    Parameters
    ----------
    frequency
        Angular frequency \\(\\omega\\) (rad/s in SI, dimensionless in natural units).
    temperature
        Temperature (K in SI, dimensionless in natural units).
    natural_units
        Use \\(\\hbar = c = k_B = 1\\).
    """
    omega = np.asarray(frequency, dtype=np.float64)
    if temperature <= 0:
        raise ValueError(f"temperature must be positive, got {temperature}")

    if natural_units:
        x = omega / temperature
        prefactor = omega**3 / (np.pi**2)
    else:
        x = (HBAR * omega) / (K_B * temperature)
        prefactor = (HBAR * omega**3) / (np.pi**2 * C**3)

    return prefactor / np.expm1(x)
