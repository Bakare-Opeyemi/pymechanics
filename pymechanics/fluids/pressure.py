import math
from pymechanics.utils.constants import g, rho_water

# ==================================================
# 1. Pressure and Hydrostatic Law
# ==================================================

def pressure(force: float, area: float) -> float:
    """
    Compute pressure.

    P = F / A
    """
    return force / area


def hydrostatic_pressure(depth: float, density: float, g: float = g) -> float:
    """
    Pressure at a depth in a static fluid.

    p = rho * g * h
    """
    return density * g * depth


def absolute_pressure(gauge_pressure: float, atmospheric_pressure: float = 101325) -> float:
    """
    Absolute pressure from gauge pressure.

    P_abs = P_gauge + P_atm
    """
    return gauge_pressure + atmospheric_pressure


def gauge_pressure(absolute_pressure: float, atmospheric_pressure: float = 101325) -> float:
    """
    Gauge pressure from absolute pressure.
    """
    return absolute_pressure - atmospheric_pressure


# ==================================================
# 2. Pascal’s Law
# ==================================================

def pascal_force(force1: float, area1: float, area2: float) -> float:
    """
    Force transmission using Pascal's law.

    F2 = F1 * (A2 / A1)
    """
    return force1 * (area2 / area1)


# ==================================================
# 3. Manometry
# ==================================================

def pressure_difference_manometer(
    density_manometric: float,
    density_fluid: float,
    height_difference: float,
    g: float = g,
) -> float:
    """
    Pressure difference measured using a differential manometer.

    Δp = (rho_m - rho_f) * g * h
    """
    return (density_manometric - density_fluid) * g * height_difference


def simple_manometer_pressure(density: float, height: float, g: float = g) -> float:
    """
    Pressure measured by a simple manometer.

    p = rho * g * h
    """
    return density * g * height


# ==================================================
# 4. Total Pressure on Submerged Surfaces
# ==================================================

def total_pressure_plane_surface(
    area: float,
    centroid_depth: float,
    density: float,
    g: float = g,
) -> float:
    """
    Total hydrostatic force on a plane surface.

    F = rho * g * A * h_c
    """
    return density * g * area * centroid_depth


# ==================================================
# 5. Centre of Pressure
# ==================================================

def centre_of_pressure_plane_surface(
    I_g: float,
    area: float,
    centroid_depth: float,
) -> float:
    """
    Depth of centre of pressure for a vertical plane surface.

    h_cp = h_c + (I_g / (A * h_c))
    """
    return centroid_depth + (I_g / (area * centroid_depth))


# ==================================================
# 6. Forces on Curved Surfaces
# ==================================================

def horizontal_force_curved_surface(
    area_vertical_projection: float,
    centroid_depth: float,
    density: float,
    g: float = g,
) -> float:
    """
    Horizontal force on a curved surface.
    """
    return density * g * area_vertical_projection * centroid_depth


def vertical_force_curved_surface(weight_of_fluid: float) -> float:
    """
    Vertical force on a curved surface.

    Equal to the weight of the imaginary fluid above the surface.
    """
    return weight_of_fluid


# ==================================================
# 7. Buoyancy and Stability
# ==================================================

def buoyant_force(density: float, displaced_volume: float, g: float = g) -> float:
    """
    Buoyant force (Archimedes' principle).

    F_b = rho * g * V
    """
    return density * g * displaced_volume


def metacentric_height(
    I_waterplane: float,
    displaced_volume: float,
    center_of_gravity: float,
    center_of_buoyancy: float,
) -> float:
    """
    Metacentric height (GM) for floating bodies.

    GM = (I / V) - BG
    """
    BG = center_of_gravity - center_of_buoyancy
    return (I_waterplane / displaced_volume) - BG
