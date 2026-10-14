import pytest
from scores import score_to_ects

def test_score_to_ects_happy_path():
    assert score_to_ects(95) == "A"

def test_score_to_ects_boundaries():
    assert score_to_ects(100) == "A"
    assert score_to_ects(90) == "A"
    assert score_to_ects(89) == "B"
    assert score_to_ects(60) == "E"
    assert score_to_ects(59) == "F"

def test_score_to_ects_failure():
    with pytest.raises(ValueError):
        score_to_ects(-1)
    
    with pytest.raises(ValueError):
        score_to_ects(101)

def test_score_to_ects_another_case():
    assert score_to_ects(62) == "E"