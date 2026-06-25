import math
from pymechanics.utils.constants import g, rho_water

# ==================================================
# 1. Pressure and Hydrostatic Law
# ==================================================

def pressure(force: float, area: float) -> float:
    """Return pressure given force and area.

    Formula: P = F / A

    Parameters:
        force (float): applied force in Newtons (N)
        area (float): area over which the force acts in square meters (m^2)

    Returns:
        float: pressure in Pascals (Pa)

    Example:
        >>> pressure(500.0, 0.25)
        2000.0
    """
    return force / area


def hydrostatic_pressure(depth: float, density: float, g: float = g) -> float:
    """Return gauge pressure at a given depth in a static fluid.

    Formula: p = rho * g * h

    Parameters:
        depth (float): depth below the free surface h in meters (m)
        density (float): fluid density rho in kg/m^3
        g (float, optional): gravitational acceleration in m/s^2 (default 9.81)

    Returns:
        float: hydrostatic gauge pressure in Pascals (Pa)

    Example:
        >>> hydrostatic_pressure(10.0, 1000.0)
        98100.0
    """
    return density * g * depth


def absolute_pressure(gauge_pressure: float, atmospheric_pressure: float = 101325) -> float:
    """Return absolute pressure from gauge pressure.

    Formula: P_abs = P_gauge + P_atm

    Parameters:
        gauge_pressure (float): gauge pressure in Pascals (Pa)
        atmospheric_pressure (float, optional): atmospheric reference pressure in Pa
            (default 101325 Pa, i.e. standard atmosphere)

    Returns:
        float: absolute pressure in Pascals (Pa)

    Example:
        >>> absolute_pressure(50000.0)
        151325.0
    """
    return gauge_pressure + atmospheric_pressure


def gauge_pressure(absolute_pressure: float, atmospheric_pressure: float = 101325) -> float:
    """Return gauge pressure from absolute pressure.

    Formula: P_gauge = P_abs - P_atm

    Parameters:
        absolute_pressure (float): absolute pressure in Pascals (Pa)
        atmospheric_pressure (float, optional): atmospheric reference pressure in Pa
            (default 101325 Pa, i.e. standard atmosphere)

    Returns:
        float: gauge pressure in Pascals (Pa); negative value indicates vacuum

    Example:
        >>> gauge_pressure(151325.0)
        50000.0
    """
    return absolute_pressure - atmospheric_pressure


# ==================================================
# 2. Pascal’s Law
# ==================================================

def pascal_force(force1: float, area1: float, area2: float) -> float:
    """Force transmission via Pascal's law.

    Formula: F2 = F1 * (A2 / A1)

    Parameters:
        force1 (float): input force in Newtons (N)
        area1 (float): input piston area in square meters (m^2); must be positive
        area2 (float): output piston area in square meters (m^2)

    Returns:
        float: output force F2 in Newtons (N)

    Example:
        >>> pascal_force(100.0, 0.01, 0.1)
        1000.0
    """
    if area1 <= 0:
        raise ValueError("area1 must be positive.")
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
    """Return pressure difference measured by a differential manometer.

    Formula: Δp = (ρ_m − ρ_f) * g * h

    Parameters:
        density_manometric (float): density of the manometric (gauge) fluid ρ_m in kg/m^3
        density_fluid (float): density of the process fluid ρ_f in kg/m^3
        height_difference (float): manometer column height difference h in meters (m)
        g (float, optional): gravitational acceleration in m/s^2 (default 9.81)

    Returns:
        float: pressure difference Δp in Pascals (Pa)

    Example:
        >>> pressure_difference_manometer(13600.0, 1000.0, 0.1)
        12361.86
    """
    return (density_manometric - density_fluid) * g * height_difference


def simple_manometer_pressure(density: float, height: float, g: float = g) -> float:
    """Return gauge pressure measured by a simple (open) manometer.

    Formula: p = ρ * g * h

    Parameters:
        density (float): manometric fluid density ρ in kg/m^3
        height (float): fluid column height h in meters (m)
        g (float, optional): gravitational acceleration in m/s^2 (default 9.81)

    Returns:
        float: gauge pressure p in Pascals (Pa)

    Example:
        >>> simple_manometer_pressure(1000.0, 0.5)
        4905.0
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
    """Return total hydrostatic force on a plane submerged surface.

    Formula: F = ρ * g * A * h_c

    Parameters:
        area (float): surface area A in square meters (m^2)
        centroid_depth (float): depth of the surface centroid h_c below the free
            surface in meters (m)
        density (float): fluid density ρ in kg/m^3
        g (float, optional): gravitational acceleration in m/s^2 (default 9.81)

    Returns:
        float: total hydrostatic force F in Newtons (N)

    Example:
        >>> total_pressure_plane_surface(2.0, 3.0, 1000.0)
        58860.0
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
    Depth to the centre of pressure on a vertical plane surface.

    h_cp = h_c + I_g / (A * h_c)

    Parameters:
        I_g (float): second moment of area of the surface about its own centroidal axis (m^4)
        area (float): total surface area (m^2)
        centroid_depth (float): depth of the centroid below the free surface h_c (m)

    Returns:
        float: depth of centre of pressure h_cp in meters (m)

    Example:
        >>> centre_of_pressure_plane_surface(1.5, 2.0, 3.0)
        3.25
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
    Horizontal component of hydrostatic force on a curved surface.

    Equals the force that would act on the vertical projection of the surface:
    F_H = rho * g * A_v * h_c

    Parameters:
        area_vertical_projection (float): area of the vertical projection of the curved surface (m^2)
        centroid_depth (float): depth of that projection's centroid below the free surface (m)
        density (float): fluid density (kg/m^3)
        g (float, optional): gravitational acceleration (m/s^2); default 9.81

    Returns:
        float: horizontal hydrostatic force F_H in Newtons (N)

    Example:
        >>> horizontal_force_curved_surface(0.5, 2.0, 1000.0)
        9810.0
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
    """Return buoyant force on a submerged or floating body (Archimedes' principle).

    Formula: F_b = ρ * g * V

    Parameters:
        density (float): fluid density ρ in kg/m^3
        displaced_volume (float): volume of fluid displaced by the body V in m^3
        g (float, optional): gravitational acceleration in m/s^2 (default 9.81)

    Returns:
        float: buoyant force F_b in Newtons (N)

    Example:
        >>> buoyant_force(1000.0, 0.5)
        4905.0
    """
    return density * g * displaced_volume


def metacentric_height(
    I_waterplane: float,
    displaced_volume: float,
    center_of_gravity: float,
    center_of_buoyancy: float,
) -> float:
    """
    Metacentric height (GM) for a floating body.

    GM = (I / V) - BG,  where BG = G - B (both measured as heights above keel)

    Parameters:
        I_waterplane (float): second moment of the waterplane area about its centroidal axis (m^4)
        displaced_volume (float): volume of fluid displaced by the body (m^3)
        center_of_gravity (float): height of the center of gravity G above the keel (m)
        center_of_buoyancy (float): height of the center of buoyancy B above the keel (m)

    Returns:
        float: metacentric height GM in meters (m); positive = stable, negative = unstable

    Example:
        >>> metacentric_height(10.0, 5.0, 3.0, 2.0)
        1.0
    """
    BG = center_of_gravity - center_of_buoyancy
    return (I_waterplane / displaced_volume) - BG
