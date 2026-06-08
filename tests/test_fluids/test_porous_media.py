import math

import pytest

from pymechanics.fluids.porous_media import properties as porous


# -----------------------------
# Porosity & compressibility
# -----------------------------

def test_porosity_from_solid_volume():
    assert porous.porosity_from_solid_volume(0.75, 1.0) == pytest.approx(0.25)


def test_porosity_from_solid_volume_rejects_nonpositive_total():
    with pytest.raises(ValueError):
        porous.porosity_from_solid_volume(0.5, 0.0)


def test_porosity_pressure_dependence():
    assert porous.porosity_pressure_dependence(0.2, 1e-9, 2e6, 1e6) == pytest.approx(0.2002)


def test_pore_compressibility():
    assert porous.pore_compressibility(2e-10, 0.2) == pytest.approx(1e-9)


def test_pore_compressibility_rejects_nonpositive_porosity():
    with pytest.raises(ValueError):
        porous.pore_compressibility(2e-10, 0.0)


# -----------------------------
# Saturation
# -----------------------------

def test_saturation_sum():
    assert porous.saturation_sum({"water": 0.6, "oil": 0.3, "gas": 0.1}) == pytest.approx(1.0)


# -----------------------------
# Wettability
# -----------------------------

@pytest.mark.parametrize(
    "theta_deg, expected",
    [
        (30, "water-wet"),
        (74.9, "water-wet"),
        (75, "intermediate-wet"),
        (90, "intermediate-wet"),
        (105, "intermediate-wet"),
        (105.1, "oil-wet"),
        (150, "oil-wet"),
    ],
)
def test_contact_angle_classification(theta_deg, expected):
    assert porous.contact_angle_classification(theta_deg) == expected


def test_amott_indices():
    result = porous.amott_indices(8, 2, 3, 7)
    assert result["delta_water"] == pytest.approx(0.8)
    assert result["delta_oil"] == pytest.approx(0.3)
    assert result["amott_harvey_index"] == pytest.approx(0.5)


def test_usbm_wettability_index():
    assert porous.usbm_wettability_index(100, 10) == pytest.approx(1.0)


def test_usbm_wettability_index_rejects_nonpositive_area():
    with pytest.raises(ValueError):
        porous.usbm_wettability_index(0, 10)


# -----------------------------
# Capillary pressure
# -----------------------------

def test_capillary_pressure_conversion():
    pc = porous.capillary_pressure_conversion(100, 0.072, 0.02, 0, 30)
    assert pc == pytest.approx(24.056261, rel=1e-5)


def test_leverett_j_function():
    j = porous.leverett_j_function(1000, 0.072, 0, 1e-12, 0.2)
    assert j == pytest.approx(0.03105650, rel=1e-5)


# -----------------------------
# Vertical equilibrium (round trip)
# -----------------------------

def test_vertical_height_and_capillary_pressure_round_trip():
    h = porous.vertical_height_from_pc(1000, 1000, 800, g=9.81)
    assert h == pytest.approx(0.5096840, rel=1e-5)
    pc = porous.capillary_pressure_from_height(h, 1000, 800, g=9.81)
    assert pc == pytest.approx(1000.0)


def test_vertical_height_rejects_nonpositive_density_difference():
    with pytest.raises(ValueError):
        porous.vertical_height_from_pc(1000, 800, 1000, g=9.81)


# -----------------------------
# Velocity & conductivity
# -----------------------------

def test_intrinsic_velocity():
    assert porous.intrinsic_velocity(0.01, 0.25) == pytest.approx(0.04)


def test_intrinsic_velocity_rejects_nonpositive_porosity():
    with pytest.raises(ValueError):
        porous.intrinsic_velocity(0.01, 0.0)


def test_hydraulic_conductivity():
    k = porous.hydraulic_conductivity(1e-12, 1000, gravity=9.81, viscosity=1e-3)
    assert k == pytest.approx(9.81e-6, rel=1e-6)


def test_hydraulic_conductivity_rejects_nonpositive_viscosity():
    with pytest.raises(ValueError):
        porous.hydraulic_conductivity(1e-12, 1000, gravity=9.81, viscosity=0.0)
