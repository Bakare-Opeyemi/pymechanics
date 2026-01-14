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
