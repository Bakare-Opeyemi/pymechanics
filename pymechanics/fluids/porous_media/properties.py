

"""
Porous media fundamental properties based on
Heinemann, Z. E. – Fluid Flow in Porous Media, Chapter 1.

This module provides computational representations of:
- Porosity and compressibility
- Phase saturation
- Wettability indices
- Capillary pressure relationships
- Leverett J-function
- Vertical equilibrium relations

All equations follow the notation and definitions used in the textbook.
"""

from dataclasses import dataclass
import math
from typing import Dict


# -----------------------------
# Porosity
# -----------------------------

def porosity(pore_volume: float, total_volume: float) -> float:
    """
    Total or effective porosity.

    φ = Vp / VT
    """
    if total_volume <= 0:
        raise ValueError("Total volume must be positive.")
    return pore_volume / total_volume


def porosity_from_solid_volume(solid_volume: float, total_volume: float) -> float:
    """
    Porosity computed from solid volume.

    φ = (VT - Vs) / VT
    """
    if total_volume <= 0:
        raise ValueError("Total volume must be positive.")
    return (total_volume - solid_volume) / total_volume


def porosity_pressure_dependence(
    phi0: float, c_phi: float, p: float, p0: float
) -> float:
    """
    Porosity variation with pressure (small compressibility approximation).

    φ ≈ φ0 [1 + cφ (p - p0)]
    """
    return phi0 * (1.0 + c_phi * (p - p0))


# -----------------------------
# Compressibility
# -----------------------------

def pore_compressibility(dphi_dp: float, phi: float) -> float:
    """
    Isothermal pore compressibility.

    cφ = (1/φ) * (∂φ/∂p)
    """
    if phi <= 0:
        raise ValueError("Porosity must be positive.")
    return dphi_dp / phi


# -----------------------------
# Saturation
# -----------------------------

def saturation(phase_volume: float, pore_volume: float) -> float:
    """
    Phase saturation.

    Si = Vi / Vp
    """
    if pore_volume <= 0:
        raise ValueError("Pore volume must be positive.")
    return phase_volume / pore_volume


def saturation_sum(saturations: Dict[str, float]) -> float:
    """
    Sum of phase saturations (should be equal to 1).
    """
    return sum(saturations.values())


# -----------------------------
# Wettability
# -----------------------------

def contact_angle_classification(theta_deg: float) -> str:
    """
    Wettability classification based on contact angle.
    """
    if theta_deg < 75:
        return "water-wet"
    elif 75 <= theta_deg <= 105:
        return "intermediate-wet"
    else:
        return "oil-wet"


def amott_indices(
    vo1: float, vo2: float, vw1: float, vw2: float
) -> Dict[str, float]:
    """
    Amott and Amott-Harvey wettability indices.

    δW = VO1 / (VO1 + VO2)
    δO = VW1 / (VW1 + VW2)
    WI = δW - δO
    """
    delta_w = vo1 / (vo1 + vo2) if (vo1 + vo2) > 0 else 0.0
    delta_o = vw1 / (vw1 + vw2) if (vw1 + vw2) > 0 else 0.0
    wi = delta_w - delta_o
    return {
        "delta_water": delta_w,
        "delta_oil": delta_o,
        "amott_harvey_index": wi,
    }


def usbm_wettability_index(a1: float, a2: float) -> float:
    """
    USBM wettability index.

    W = log10(A1 / A2)
    """
    if a1 <= 0 or a2 <= 0:
        raise ValueError("Areas must be positive.")
    return math.log10(a1 / a2)


# -----------------------------
# Capillary Pressure
# -----------------------------

def capillary_pressure(
    sigma: float, theta_deg: float, r1: float, r2: float = math.inf
) -> float:
    """
    Laplace equation for capillary pressure.

    Pc = σ (1/r1 + 1/r2)
    """
    theta = math.radians(theta_deg)
    cos_theta = math.cos(theta)
    curvature = (1.0 / r1) + (0.0 if math.isinf(r2) else (1.0 / r2))
    return sigma * cos_theta * curvature


def capillary_pressure_conversion(
    pc_lab: float,
    sigma_lab: float,
    sigma_res: float,
    theta_lab_deg: float,
    theta_res_deg: float,
) -> float:
    """
    Convert laboratory capillary pressure to reservoir conditions.

    PcR = PcL * (σR cosθR) / (σL cosθL)
    """
    cos_lab = math.cos(math.radians(theta_lab_deg))
    cos_res = math.cos(math.radians(theta_res_deg))
    return pc_lab * (sigma_res * cos_res) / (sigma_lab * cos_lab)


# -----------------------------
# Leverett J-function
# -----------------------------

def leverett_j_function(
    pc: float,
    sigma: float,
    theta_deg: float,
    permeability: float,
    porosity: float,
) -> float:
    """
    Leverett J-function.

    J(Sw) = Pc / (σ cosθ) * sqrt(k / φ)
    """
    theta = math.radians(theta_deg)
    return (pc / (sigma * math.cos(theta))) * math.sqrt(permeability / porosity)


# -----------------------------
# Vertical Equilibrium
# -----------------------------

def vertical_height_from_pc(
    pc: float, rho_w: float, rho_nw: float, g: float = 9.81
) -> float:
    """
    Height above Pc = 0 plane.

    h = Pc / [(ρw - ρnw) g]
    """
    delta_rho = rho_w - rho_nw
    if delta_rho <= 0:
        raise ValueError("Wetting phase density must exceed non-wetting phase density.")
    return pc / (delta_rho * g)


def capillary_pressure_from_height(
    h: float, rho_w: float, rho_nw: float, g: float = 9.81
) -> float:
    """
    Capillary pressure as a function of height.

    Pc = (ρw - ρnw) g h
    """
    return (rho_w - rho_nw) * g * h