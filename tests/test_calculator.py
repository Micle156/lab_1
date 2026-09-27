import argparse

import pytest

from toolkit.__main__ import run_calc
from toolkit.calculator import ans
from toolkit.validation import ValidationError

"""правильные тесты"""

def test_1():
    assert ans("2+4*3") == 14

def test_2():
    assert ans("100    /   5") == 20

def test_3():
    assert ans("6/4.0") == 1.5

def test_4():
    assert ans("2+9.34") == 11.34

def test_5():
    assert ans("5 -10") == -5

def test_6():
    assert ans("10/4") == 2.5

def test_7():
    assert ans("-2*-3") == 6

def test_8():
    assert ans("1+-2") == -1

def test_9():
    assert ans("(3 +4)*9") == 63

def test_10():
    assert ans("-(2+3)") == -5

def test_11():
    assert ans("3+ (-3)") == 0


"""неправильные тесты"""

def test_n_1():
    args = argparse.Namespace(expression = "")
    with pytest.raises(ValidationError):
        run_calc(args)

def test_n_2():
    args = argparse.Namespace(expression = "34 / 0")
    with pytest.raises(ZeroDivisionError):
        run_calc(args)

def test_n_3():
    args = argparse.Namespace(expression = "++43 - 35")
    with pytest.raises(ValidationError):
        run_calc(args)

def test_n_4():
    args = argparse.Namespace(expression = "55 - 67*")
    with pytest.raises(ValidationError):
        run_calc(args)

def test_n_5():
    args = argparse.Namespace(expression = "34 -* 4")
    with pytest.raises(ValidationError):
        run_calc(args)

def test_n_6():
    args = argparse.Namespace(expression = "+56 +++43")
    with pytest.raises(ValidationError):
        run_calc(args)

def test_n_7():
    args = argparse.Namespace(expression = "55 + (3-0))")
    with pytest.raises(ValidationError):
        run_calc(args)

def test_n_8():
    args = argparse.Namespace(expression = "90-45*3")
    assert run_calc(args) == 45