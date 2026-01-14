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
    "A fluid has a mass of 250 kg and occupies a volume of 0.2 m^3. "
    "(a) Determine the density of the fluid. "
    "(b) Determine its specific weight."
)

QUESTION_2 = (
    "The density of an oil is 850 kg/m^3. "
    "Determine the specific gravity of the oil."
)

QUESTION_3 = (
    "A fluid has a dynamic viscosity of 0.9 Ns/m^2 and a density of 900 kg/m^3. "
    "Determine the kinematic viscosity of the fluid."
)

QUESTION_4 = (
    "The velocity gradient between two parallel fluid layers is 40 s^-1. "
    "If the dynamic viscosity is 0.8 Ns/m^2, determine the shear stress."
)

QUESTION_5 = (
    "Determine the capillary rise in a glass tube of 2 mm diameter when water flows through it. "
    "Take surface tension = 0.072 N/m, contact angle = 0 degrees, "
    "and density of water = 1000 kg/m^3."
)

QUESTION_6 = (
    "The local pressure at a point in a flowing fluid is 2.5 kPa. "
    "The vapor pressure of the fluid is 3 kPa. "
    "Determine whether cavitation will occur."
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
# Example Usage
# ==================================================
# from pymechanics.exercises.exercise_1_1_examples import get_question
# print(get_question(3))
