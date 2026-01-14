"""Surface and interfacial fluid phenomena helpers.

Formulas and notes:
- Pressure jump due to surface tension (spherical interface):
        Delta P = 2 * gamma / R
    where gamma is surface tension (N/m) and R is radius (m).

- Capillary rise in a vertical tube (using diameter d):
        h = (2 * gamma * cos(theta)) / (rho * g * r)
    with r = d/2, this becomes:
        h = (4 * gamma * cos(theta)) / (rho * g * d)
    where h is rise height (m), theta is contact angle (rad),
    rho is fluid density (kg/m^3), g is gravitational acceleration (m/s^2),
    and d is tube diameter (m).

- Cavitation risk (simple check): occurs when local pressure <= vapor pressure.

Units (typical SI):
- surface_tension: N/m
- radius, diameter, height: m
- density: kg/m^3
- g: m/s^2
- pressure: Pa (N/m^2)

These functions use simple idealized formulas; they do not attempt to
capture complex geometries or dynamic effects.
"""

import math


def pressure_due_to_surface_tension(surface_tension, radius):
    """Return the pressure jump across a curved surface due to surface tension.

    Formula: Delta P = 2 * gamma / R

    Parameters:
        surface_tension (float): surface tension gamma in N/m
        radius (float): radius of curvature R in m

    Returns:
        float: pressure difference (Pa)
    """
    return 2 * surface_tension / radius


def capillary_rise(surface_tension, contact_angle, density, diameter, g=9.81):
    """Return capillary rise height in a vertical circular tube.

    Formula (using diameter d):
        h = (4 * gamma * cos(theta)) / (rho * g * d)

    Parameters:
        surface_tension (float): surface tension gamma in N/m
        contact_angle (float): contact angle theta in radians
        density (float): fluid density rho in kg/m^3
        diameter (float): tube inner diameter d in m
        g (float, optional): gravitational acceleration in m/s^2 (default 9.81)

    Returns:
        float: capillary rise height h in meters (m)
    """
    return round((4 * surface_tension * math.cos(contact_angle)) / (density * g * diameter), 4)


def cavitation_risk(local_pressure, vapor_pressure):
    """Simple boolean check for cavitation risk.

    Returns True when the local static pressure is less than or equal to
    the vapor pressure of the fluid (i.e., conditions where vapor bubbles
    may form), otherwise False.

    Parameters:
        local_pressure (float): local static pressure in Pa
        vapor_pressure (float): fluid vapor pressure in Pa

    Returns:
        bool: True if cavitation is possible, False otherwise
    """
    return local_pressure <= vapor_pressure