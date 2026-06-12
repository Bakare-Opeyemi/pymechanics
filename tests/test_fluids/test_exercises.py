import pytest
from pymechanics.fluids.exercises import properties as ex


# ---- Exercise 1.1 questions ----

def test_get_question_returns_nonempty_string():
    for n in range(1, 7):
        assert isinstance(ex.get_question(n), str)
        assert len(ex.get_question(n)) > 0


def test_get_question_known_content():
    # Q1 is about mass density of an oil
    assert "density" in ex.get_question(1).lower() or "mass" in ex.get_question(1).lower()


def test_get_question_invalid_raises():
    with pytest.raises(ValueError):
        ex.get_question(0)
    with pytest.raises(ValueError):
        ex.get_question(7)


# ---- Exercise 1.1 answers ----

def test_get_answer_returns_nonempty_string():
    for n in range(1, 7):
        assert isinstance(ex.get_answer(n), str)
        assert len(ex.get_answer(n)) > 0


def test_get_answer_invalid_raises():
    with pytest.raises(ValueError):
        ex.get_answer(0)
    with pytest.raises(ValueError):
        ex.get_answer(7)


# ---- Exercise 1.2 questions ----

def test_get_exercise_1_2_question_returns_nonempty_string():
    for n in range(1, 6):
        assert isinstance(ex.get_exercise_1_2_question(n), str)
        assert len(ex.get_exercise_1_2_question(n)) > 0


def test_get_exercise_1_2_question_invalid_raises():
    with pytest.raises(ValueError):
        ex.get_exercise_1_2_question(0)
    with pytest.raises(ValueError):
        ex.get_exercise_1_2_question(6)


# ---- Exercise 1.2 answers ----

def test_get_exercise_1_2_answer_returns_nonempty_string():
    for n in range(1, 6):
        assert isinstance(ex.get_exercise_1_2_answer(n), str)
        assert len(ex.get_exercise_1_2_answer(n)) > 0


def test_get_exercise_1_2_answer_invalid_raises():
    with pytest.raises(ValueError):
        ex.get_exercise_1_2_answer(0)
    with pytest.raises(ValueError):
        ex.get_exercise_1_2_answer(6)
