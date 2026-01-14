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
    "Determine the mass density of an oil, if 3.0 tonnes of the oil occupies a volume of 4 m^3."
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
# from pymechanics.fluids.exercises.exercise_1_1 import get_question, get_answer
# print(get_question(3))
# print(get_answer(3))
