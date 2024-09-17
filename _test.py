import pytest
from calculator import Operations



def test_addition():
    calc = Operations(5, 3)
    assert calc.addition() == 8

def test_subtraction():
    calc = Operations(5, 3)
    assert calc.subtraction() == 2

def test_multiplication():
    calc = Operations(5, 3)
    assert calc.multiplication() == 15

def test_division():
    calc = Operations(6, 3)
    assert calc.division() == 2.0

def test_division_by_zero():
    calc = Operations(5, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc.division()

def test_power():
    calc = Operations(2, 3)
    assert calc.power() == 8


