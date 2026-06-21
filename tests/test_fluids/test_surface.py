import math
from pymechanics.fluids import surface
import pytest


def test_pressure_due_to_surface_tension():
    assert surface.pressure_due_to_surface_tension(0.072, 0.001) == pytest.approx(144)


def test_capillary_rise_khurmi_example():
    sigma = 0.074
    theta = math.radians(5)
    rho = 1000
    d = 5e-3
    h = surface.capillary_rise(sigma, theta, rho, d)
    assert h == pytest.approx(6.0e-3, rel=1e-3)


def test_cavitation_risk():
    assert surface.cavitation_risk(2500, 3000) is True
    assert surface.cavitation_risk(4000, 3000) is False


def test_cavitation_risk_equal_pressures():
    # local == vapor pressure is exactly the threshold; cavitation is possible
    assert surface.cavitation_risk(3000, 3000) is True


def test_pressure_due_to_surface_tension_proportional_to_inverse_radius():
    # halving the radius must double the pressure jump
    p_small = surface.pressure_due_to_surface_tension(0.072, 0.01)
    p_large = surface.pressure_due_to_surface_tension(0.072, 0.02)
    assert p_small == pytest.approx(2 * p_large)


def test_capillary_rise_neutral_contact_angle():
    # at 90 deg the cosine is 0, so there is no capillary rise
    h = surface.capillary_rise(0.072, math.pi / 2, 1000, 0.001)
    assert h == pytest.approx(0.0, abs=1e-10)


def test_capillary_rise_hydrophobic_gives_depression():
    # contact angle > 90 deg (hydrophobic) produces capillary depression (h < 0)
    h = surface.capillary_rise(0.072, math.radians(120), 1000, 0.001)
    assert h < 0
    assert h == pytest.approx(-0.0147, rel=1e-3)


def test_capillary_rise_custom_gravity():
    # verify that a non-default g (lunar: ~1.62 m/s^2) scales the result correctly
    sigma, theta, rho, d = 0.072, 0.0, 1000, 0.001
    h_moon = surface.capillary_rise(sigma, theta, rho, d, g=1.62)
    h_earth = surface.capillary_rise(sigma, theta, rho, d, g=9.81)
    # rounding to 4 dp inside capillary_rise limits precision; use 1 % tolerance
    assert h_moon == pytest.approx(h_earth * 9.81 / 1.62, rel=1e-2)


def test_pressure_due_to_surface_tension_rejects_zero_radius():
    with pytest.raises(ValueError):
        surface.pressure_due_to_surface_tension(0.072, 0.0)


def test_pressure_due_to_surface_tension_rejects_negative_radius():
    with pytest.raises(ValueError):
        surface.pressure_due_to_surface_tension(0.072, -0.001)


def test_capillary_rise_rejects_zero_diameter():
    with pytest.raises(ValueError):
        surface.capillary_rise(0.072, 0.0, 1000, 0.0)


def test_capillary_rise_rejects_negative_diameter():
    with pytest.raises(ValueError):
        surface.capillary_rise(0.072, 0.0, 1000, -0.001)


def test_capillary_rise_rejects_zero_density():
    with pytest.raises(ValueError):
        surface.capillary_rise(0.072, 0.0, 0.0, 0.001)
