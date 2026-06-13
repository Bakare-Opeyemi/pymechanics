import pytest
from pymechanics.fluids import pressure


def test_pressure_basic():
    assert pressure.pressure(1000.0, 0.5) == pytest.approx(2000.0)


def test_hydrostatic_pressure():
    # rho=1000 kg/m^3, g=9.81, h=10 m -> 98100 Pa
    assert pressure.hydrostatic_pressure(10.0, 1000.0) == pytest.approx(98100.0)


def test_absolute_pressure_default_atm():
    assert pressure.absolute_pressure(50000.0) == pytest.approx(151325.0)


def test_absolute_pressure_at_zero_gauge():
    assert pressure.absolute_pressure(0.0) == pytest.approx(101325.0)


def test_gauge_pressure():
    assert pressure.gauge_pressure(151325.0) == pytest.approx(50000.0)


def test_gauge_pressure_at_atmospheric():
    assert pressure.gauge_pressure(101325.0) == pytest.approx(0.0)


def test_absolute_gauge_roundtrip():
    p_abs = pressure.absolute_pressure(30000.0)
    assert pressure.gauge_pressure(p_abs) == pytest.approx(30000.0)


def test_pascal_force():
    # F2 = 100 * (0.1 / 0.01) = 1000 N
    assert pressure.pascal_force(100.0, 0.01, 0.1) == pytest.approx(1000.0)


def test_pressure_difference_manometer():
    # mercury (13600) vs water (1000), h=0.1 m
    expected = (13600.0 - 1000.0) * 9.81 * 0.1
    assert pressure.pressure_difference_manometer(13600.0, 1000.0, 0.1) == pytest.approx(expected)


def test_simple_manometer_pressure():
    assert pressure.simple_manometer_pressure(1000.0, 0.5) == pytest.approx(4905.0)


def test_total_pressure_plane_surface():
    # F = rho*g*A*h_c = 1000*9.81*2.0*3.0
    assert pressure.total_pressure_plane_surface(2.0, 3.0, 1000.0) == pytest.approx(58860.0)


def test_centre_of_pressure_plane_surface():
    # h_cp = 3.0 + 1.5/(2.0*3.0) = 3.25 m
    assert pressure.centre_of_pressure_plane_surface(1.5, 2.0, 3.0) == pytest.approx(3.25)


def test_horizontal_force_curved_surface():
    # F_h = rho * g * A_v * h_c = 1000 * 9.81 * 0.5 * 2.0 = 9810 N
    assert pressure.horizontal_force_curved_surface(0.5, 2.0, 1000.0) == pytest.approx(9810.0)


def test_vertical_force_curved_surface():
    # Returns the weight of fluid above the curved surface directly
    assert pressure.vertical_force_curved_surface(4905.0) == pytest.approx(4905.0)


def test_buoyant_force():
    # F_b = 1000 * 9.81 * 0.5 = 4905 N
    assert pressure.buoyant_force(1000.0, 0.5) == pytest.approx(4905.0)


def test_metacentric_height():
    # GM = (10/5) - (3.0 - 2.0) = 1.0 m
    assert pressure.metacentric_height(10.0, 5.0, 3.0, 2.0) == pytest.approx(1.0)


def test_hydrostatic_pressure_custom_gravity():
    # Lunar gravity (~1.62 m/s^2): pressure at same depth scales proportionally
    p_moon = pressure.hydrostatic_pressure(10.0, 1000.0, g=1.62)
    assert p_moon == pytest.approx(16200.0)


def test_gauge_pressure_vacuum():
    # Absolute pressure below atmospheric gives a negative gauge pressure (vacuum)
    p_gauge = pressure.gauge_pressure(50000.0)
    assert p_gauge == pytest.approx(50000.0 - 101325.0)
    assert p_gauge < 0


def test_buoyant_force_custom_gravity():
    # Martian gravity (~3.72 m/s^2): F_b = 1000 * 3.72 * 0.5 = 1860 N
    assert pressure.buoyant_force(1000.0, 0.5, g=3.72) == pytest.approx(1860.0)


def test_metacentric_height_negative_unstable():
    # GM < 0 means G is above M — the body is unstable
    # GM = (1.0/5.0) - (4.0 - 2.0) = 0.2 - 2.0 = -1.8 m
    gm = pressure.metacentric_height(1.0, 5.0, 4.0, 2.0)
    assert gm == pytest.approx(-1.8)
    assert gm < 0


def test_pascal_force_equal_areas():
    # Identical piston areas: output force equals input force
    assert pressure.pascal_force(500.0, 0.05, 0.05) == pytest.approx(500.0)
