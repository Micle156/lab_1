import argparse

import pytest

from toolkit.__main__ import run_convert
from toolkit.converter import conv
from toolkit.validation import ValidationError

"""правильные тесты"""

def test_1():
    assert conv("10", "km", "m") == 10000.0

def test_2():
    assert conv("-273.15", "c", "k") == 0

def test_3():
    assert conv("0", "c", "f") == 32.0

def test_4():
    assert conv("900", "CM", "M") == 9

def test_5():
    assert conv("32", "f", "K") == 273.15

def test_6():
    assert conv("1.5", "kG", "G") == 1500

def test_7():
    assert conv("1000", "Mm", "m") == 1.0

def test_8():
    assert conv("0.67", "Km", "mM") == 670000.0

def test_9():
    assert conv("0.67", "km", "Cm") == 67000.0

def test_10():
    assert conv("0.9", "cm", "mM") == 9.0

"""неправильные тесты"""

def test_n_1():
    args = argparse.Namespace(value = "23.3.3", 
                              from_unit = 'c', 
                              to_unit = 'k')
    with pytest.raises(ValidationError):
        run_convert(args)

def test_n_2():
    args = argparse.Namespace(value = "-2.54", 
                              from_unit = 'k', 
                              to_unit = 'c')
    with pytest.raises(ValidationError):
        run_convert(args)

def test_n_3():
    args = argparse.Namespace(value = "23",
                              from_unit = 'mil', 
                              to_unit = 'cm')
    with pytest.raises(ValidationError):
        run_convert(args)

def test_n_4():
    args = argparse.Namespace(value = "58", 
                              from_unit = 'kg', 
                              to_unit = 'm')
    with pytest.raises(ValidationError):
        run_convert(args)

def test_n_5():
    args = argparse.Namespace(value = "twelve", 
                              from_unit = 'c', 
                              to_unit = 'k')
    with pytest.raises(ValidationError):
        run_convert(args)

def test_n_6():
    args = argparse.Namespace(value = "34", 
                              from_unit = 'kg', 
                              to_unit = "")
    with pytest.raises(ValidationError):
        run_convert(args)

def test_n_7():
    args = argparse.Namespace(value = "76.", 
                              from_unit = 'cm', 
                              to_unit = 'm')
    with pytest.raises(ValidationError):
        run_convert(args)

def test_n_8():
    args = argparse.Namespace(value = ".34", 
                              from_unit = 'kg', 
                              to_unit = 'g')
    with pytest.raises(ValidationError):
        run_convert(args)
