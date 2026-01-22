"""
Exercise 1.1 – Example Problems (Questions 1–6)
Reference: Khurmi & Gupta – Hydraulics, Fluid Mechanics and Hydraulic Machines
Chapter 1: Properties of Fluids

This module exposes Exercise 1.1 questions as Python strings so users
can programmatically retrieve, display, or solve them.
"""

# ==================================================
# Exercise 1.1 – Questions as Strings
# ==================================================

QUESTION_1 = (
    "Determine the mass density of an oil, if 3.00 tonnes of the oil occupies a volume of 4 m^3."
)

QUESTION_2 = (
    "A certain liquid, occupying a volume of 1.6 m^3, weighs 12.8 kN. What is the specific weight of the liquid?"
)

QUESTION_3 = (
    "A container of volume 3.0 m^3 has 25.5 kN of an oil. Find the specific weight and mass density of the oil."
)

QUESTION_4 = (
    "What is the specific gravity of a liquid, whose specific weight is 7.36 kN/m^3?"
)

QUESTION_5 = (
    "A drum of 1 m^3 volume contains 8.5 kN an oil when full. Find its specific weight and specific gravity."
)

QUESTION_6 = (
    "A 5 mm diameter glass tube is immersed vertically in water. If the contact angle is 5°, find the capillary rise. Take surface tension for the water as 0.074 N/m."
)


# ==================================================
# Public API
# ==================================================

EXERCISE_1_1 = {
    1: QUESTION_1,
    2: QUESTION_2,
    3: QUESTION_3,
    4: QUESTION_4,
    5: QUESTION_5,
    6: QUESTION_6,
}


def get_question(number: int) -> str:
    """
    Return a specific Exercise 1.1 question.

    Parameters
    ----------
    number : int
        Question number (1–6)

    Returns
    -------
    str
        The requested question as a string
    """
    if number not in EXERCISE_1_1:
        raise ValueError("Question number must be between 1 and 6")
    return EXERCISE_1_1[number]


# ==================================================
# Exercise 1.1 – Answers as Strings
# ==================================================

ANSWER_1 = (
    "Mass density = 3.0 tonnes / 4 m^3 = 3000 kg / 4 m^3 = 750 kg/m^3."
)

ANSWER_2 = (
    "Specific weight = weight / volume = 12.8 kN / 1.6 m^3 = 8 kN/m^3."
)

ANSWER_3 = (
    "Specific weight = 25.5 kN / 3.0 m^3 = 8.5 kN/m^3. "
    "Mass density = specific_weight / g = 8500 N/m^3 / 9.81 m/s^2 ≈ 866 kg/m^3."
)

ANSWER_4 = (
    "Specific gravity = specific_weight / (rho_water * g) = 7360 N/m^3 / 9810 N/m^3 = 0.75."
)

ANSWER_5 = (
    "Specific weight = 8.5 kN / 1 m^3 = 8.5 kN/m^3. "
    "Specific gravity = 8500 / 9810 ≈ 0.866."
)

ANSWER_6 = (
    "Capillary rise h = 4 * sigma * cos(alpha) / (rho * g * d). "
    "Using sigma=0.074 N/m, alpha=5°, rho=1000 kg/m^3, d=5e-3 m: "
    "h ≈ 6.0e-3 m = 6 mm."
)

EXERCISE_1_1_ANSWERS = {
    1: ANSWER_1,
    2: ANSWER_2,
    3: ANSWER_3,
    4: ANSWER_4,
    5: ANSWER_5,
    6: ANSWER_6,
}


def get_answer(number: int) -> str:
    """
    Return the answer string for a specific Exercise 1.1 question.

    Parameters
    ----------
    number : int
        Question number (1–6)

    Returns
    -------
    str
        The requested answer as a string
    """
    if number not in EXERCISE_1_1_ANSWERS:
        raise ValueError("Question number must be between 1 and 6")
    return EXERCISE_1_1_ANSWERS[number]


# ==================================================
# Example Usage
# ==================================================
# Example usage:
# from pymechanics.fluids.exercises.properties import get_question, get_answer
# print(get_question(3))
# print(get_answer(3))

# ==================================================
# Exercise 1.2 – Numerical Problems (Chapter 1)
# ==================================================

QUESTION_1_2_1 = (
    "The mass density of a liquid is 850 kg/m^3. Determine its specific weight "
    "and specific gravity. Take g = 9.81 m/s^2."
)

QUESTION_1_2_2 = (
    "A liquid has a bulk modulus of elasticity of 2.1 GPa. Determine the "
    "change in pressure required to produce a volumetric strain of 0.1%."
)

QUESTION_1_2_3 = (
    "The volume of a liquid decreases by 0.02% when the pressure is increased "
    "by 4 MPa. Determine the bulk modulus of the liquid."
)

QUESTION_1_2_4 = (
    "Determine the capillary rise in a glass tube of 4 mm diameter when "
    "immersed in water. Take surface tension = 0.072 N/m, contact angle = 0°, "
    "and density of water = 1000 kg/m^3."
)

QUESTION_1_2_5 = (
    "A liquid weighs 9 kN/m^3. Determine its mass density and specific gravity."
)


EXERCISE_1_2 = {
    1: QUESTION_1_2_1,
    2: QUESTION_1_2_2,
    3: QUESTION_1_2_3,
    4: QUESTION_1_2_4,
    5: QUESTION_1_2_5,
}


def get_exercise_1_2_question(number: int) -> str:
    """
    Return a specific Exercise 1.2 question.

    Parameters
    ----------
    number : int
        Question number (1–5)

    Returns
    -------
    str
        The requested question as a string
    """
    if number not in EXERCISE_1_2:
        raise ValueError("Question number must be between 1 and 5")
    return EXERCISE_1_2[number]


# ==================================================
# Exercise 1.2 – Answers as Strings
# ==================================================

ANSWER_1_2_1 = (
    "Specific weight = ρ g = 850 × 9.81 = 8338.5 N/m^3 ≈ 8.34 kN/m^3. "
    "Specific gravity = ρ / ρ_water = 850 / 1000 = 0.85."
)

ANSWER_1_2_2 = (
    "Bulk modulus K = Δp / (ΔV / V). "
    "ΔV / V = 0.1% = 0.001. "
    "Δp = K × (ΔV / V) = 2.1×10^9 × 0.001 = 2.1×10^6 Pa = 2.1 MPa."
)

ANSWER_1_2_3 = (
    "Bulk modulus K = Δp / (ΔV / V). "
    "ΔV / V = 0.02% = 0.0002. "
    "K = 4×10^6 / 0.0002 = 2.0×10^10 Pa = 20 GPa."
)

ANSWER_1_2_4 = (
    "Capillary rise h = 4 σ cosθ / (ρ g d). "
    "h = (4 × 0.072 × cos0°) / (1000 × 9.81 × 0.004) "
    "≈ 7.34×10^-3 m = 7.34 mm."
)

ANSWER_1_2_5 = (
    "Mass density ρ = γ / g = 9000 / 9.81 ≈ 917 kg/m^3. "
    "Specific gravity = ρ / 1000 ≈ 0.917."
)


EXERCISE_1_2_ANSWERS = {
    1: ANSWER_1_2_1,
    2: ANSWER_1_2_2,
    3: ANSWER_1_2_3,
    4: ANSWER_1_2_4,
    5: ANSWER_1_2_5,
}


def get_exercise_1_2_answer(number: int) -> str:
    """
    Return the answer string for a specific Exercise 1.2 question.

    Parameters
    ----------
    number : int
        Question number (1–5)

    Returns
    -------
    str
        The requested answer as a string
    """
    if number not in EXERCISE_1_2_ANSWERS:
        raise ValueError("Question number must be between 1 and 5")
    return EXERCISE_1_2_ANSWERS[number]
