import pytest
from pymechanics.fluids import properties


def test_density():
    assert properties.density(3000, 4) == pytest.approx(750)


def test_specific_weight():
    # 750 kg/m^3 * 9.81 m/s^2
    assert properties.specific_weight(750) == pytest.approx(750 * 9.81)


def test_specific_gravity():
    assert properties.specific_gravity(850) == pytest.approx(0.85)


def test_kinematic_viscosity():
    assert properties.kinematic_viscosity(0.9, 900) == pytest.approx(0.001)


def test_shear_stress():
    assert properties.shear_stress(0.8, 40) == pytest.approx(32)


def test_bulk_modulus():
    assert properties.bulk_modulus(200000.0, 0.01) == pytest.approx(200000.0 / 0.01)
