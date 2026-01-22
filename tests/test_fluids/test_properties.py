import pytest
from pymechanics.fluids import properties
from pymechanics.fluids.porous_media import properties as porous_properties


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


# -----------------------------
# Porous media – Chapter 1 examples
# -----------------------------

def test_porosity_example():
    # Example: pore volume = 0.25 m^3, total volume = 1.0 m^3
    assert porous_properties.porosity(0.25, 1.0) == pytest.approx(0.25)


def test_saturation_example():
    # Example: water volume = 0.18 m^3, pore volume = 0.30 m^3
    assert porous_properties.saturation(0.18, 0.30) == pytest.approx(0.6)


def test_darcy_velocity_example():
    # Example values from Darcy-law illustration
    # k = 1e-12 m^2, mu = 1e-3 Pa·s, dp/dx = 1e5 Pa/m
    v = porous_properties.darcy_velocity(
        permeability=1e-12,
        viscosity=1e-3,
        pressure_gradient=1e5,
    )
    assert v == pytest.approx(-1e-4)


def test_darcy_flow_rate_example():
    # Example core flooding calculation
    # k = 2e-13 m^2, A = 1e-3 m^2, mu = 1e-3 Pa·s
    # Δp = 5e4 Pa, L = 0.2 m
    q = porous_properties.darcy_flow_rate(
        permeability=2e-13,
        viscosity=1e-3,
        area=1e-3,
        pressure_drop=5e4,
        length=0.2,
    )
    assert q == pytest.approx(-5e-8)


def test_permeability_from_darcy_example():
    # Inversion of Darcy experiment
    # Q = 1e-7 m^3/s, mu = 1e-3 Pa·s, L = 0.1 m
    # A = 5e-4 m^2, Δp = 2e5 Pa
    k = porous_properties.permeability_from_darcy(
        flow_rate=1e-7,
        viscosity=1e-3,
        length=0.1,
        area=5e-4,
        pressure_drop=2e5,
    )
    assert k == pytest.approx(1e-13)


def test_capillary_pressure_example():
    # Laplace capillary pressure example
    # sigma = 0.03 N/m, theta = 0 deg, r = 1e-6 m
    pc = porous_properties.capillary_pressure(
        sigma=0.03,
        theta_deg=0.0,
        r1=1e-6,
    )
    assert pc == pytest.approx(3e4)


def test_equivalent_permeability_series_example():
    # Two-layer system, flow normal to layers
    k = porous_properties.equivalent_permeability_series(
        permeabilities={"L1": 1e-13, "L2": 5e-13},
        lengths={"L1": 0.4, "L2": 0.6},
    )
    assert k == pytest.approx(2.0833333333333335e-13)


def test_equivalent_permeability_parallel_example():
    # Two-layer system, flow parallel to layers
    k = porous_properties.equivalent_permeability_parallel(
        permeabilities={"L1": 1e-13, "L2": 5e-13},
        thicknesses={"L1": 0.4, "L2": 0.6},
    )
    assert k == pytest.approx(3.4e-13)
