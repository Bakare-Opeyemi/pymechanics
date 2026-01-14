"""Fluid property helper functions with formulas and brief explanations.

Formulas (summary):
    - Density: rho = m / V
    - Specific weight: gamma = rho * g
    - Specific gravity: SG = rho / rho_water
    - Kinematic viscosity: nu = mu / rho
    - Shear stress (Newtonian): tau = mu * (du/dy)
    - Bulk modulus: K = delta_p / (DeltaV/V) = delta_p / volumetric_strain

Units (typical SI):
    - mass: kg
    - volume: m^3
    - density (rho): kg/m^3
    - g (gravity): m/s^2
    - dynamic viscosity (mu): Pa·s (N·s/m^2)
    - kinematic viscosity (nu): m^2/s
    - shear stress (tau): Pa (N/m^2)
    - bulk modulus (K): Pa

Each function below implements a simple and direct formula used in
basic fluid mechanics. Inputs are expected to be numeric scalars
in SI units unless otherwise stated.
"""

def density(mass, volume):
    """Return density (rho) given mass and volume.

    Formula: rho = m / V

    Parameters:
        mass (float): mass in kilograms (kg)
        volume (float): volume in cubic meters (m^3)

    Returns:
        float: density in kilograms per cubic meter (kg/m^3)
    """
    return mass / volume

def specific_weight(density, g=9.81):
    
    """Return specific weight (gamma) of a fluid.

    Formula: gamma = rho * g

    Parameters:
        density (float): fluid density (kg/m^3)
        g (float, optional): gravitational acceleration (m/s^2). Default 9.81.

    Returns:
        float: specific weight in N/m^3 (equivalently kg/(m^2·s^2))
    """
    return density * g

def specific_gravity(density, rho_water=1000):
    """Return specific gravity (dimensionless) relative to water.

    Formula: SG = rho / rho_water

    Parameters:
        density (float): fluid density (kg/m^3)
        rho_water (float, optional): reference density for water (kg/m^3).
            Default is 1000 kg/m^3 at ~4°C.

    Returns:
        float: specific gravity (dimensionless)
    """
    return density / rho_water

def kinematic_viscosity(dynamic_viscosity, density):
    """Return kinematic viscosity (nu).

    Formula: nu = mu / rho

    Parameters:
        dynamic_viscosity (float): dynamic (absolute) viscosity mu in Pa·s
        density (float): fluid density rho in kg/m^3

    Returns:
        float: kinematic viscosity nu in m^2/s
    """
    return dynamic_viscosity / density

def shear_stress(mu, velocity_gradient):
    """Return shear stress for a Newtonian fluid.

    Formula (Newtonian): tau = mu * (du/dy)

    Parameters:
        mu (float): dynamic viscosity (Pa·s)
        velocity_gradient (float): velocity gradient du/dy in 1/s

    Returns:
        float: shear stress tau in Pa (N/m^2)
    """
    return mu * velocity_gradient


def bulk_modulus(delta_p, volumetric_strain):
    """Return bulk modulus K from pressure change and volumetric strain.

    Formula: K = delta_p / (DeltaV/V) = delta_p / volumetric_strain

    Parameters:
        delta_p (float): change in pressure (Pa)
        volumetric_strain (float): relative change in volume (DeltaV/V),
            dimensionless. Must be non-zero.

    Returns:
        float: bulk modulus in Pascals (Pa)
    """
    return delta_p / volumetric_strain

