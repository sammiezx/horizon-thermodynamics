"""Sanity tests for the Hawking-radiation formulas."""

import numpy as np
import pytest

from bh_radiation.hawking import hawking_temperature, planck_spectrum


def test_solar_mass_temperature_is_tiny():
    M_sun = 1.989e30  # kg
    T = hawking_temperature(M_sun)
    assert 5e-8 < T < 7e-8


def test_natural_units_temperature():
    # T_H = 1 / (8 pi M); for M=1, T = 1/(8 pi)
    assert hawking_temperature(1.0, natural_units=True) == pytest.approx(
        1.0 / (8.0 * np.pi)
    )


def test_temperature_inverse_in_mass():
    assert hawking_temperature(2.0, natural_units=True) == pytest.approx(
        0.5 * hawking_temperature(1.0, natural_units=True)
    )


def test_negative_mass_rejected():
    with pytest.raises(ValueError):
        hawking_temperature(-1.0)


def test_planck_spectrum_positive_finite():
    omega = np.linspace(0.1, 10.0, 50)
    u = planck_spectrum(omega, temperature=1.0, natural_units=True)
    assert np.all(np.isfinite(u))
    assert np.all(u > 0)


def test_planck_spectrum_wien_tail_decays():
    # Above x = hbar omega / kT >> 1, spectrum decays as exp(-x).
    u_low = planck_spectrum(5.0, temperature=1.0, natural_units=True)
    u_high = planck_spectrum(20.0, temperature=1.0, natural_units=True)
    assert u_high < u_low
