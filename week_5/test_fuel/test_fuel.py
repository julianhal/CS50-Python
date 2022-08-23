# Solution to https://cs50.harvard.edu/python/2022/psets/5/test_fuel/

from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/3") == 33
    assert convert("3/4") == 75
    assert convert("0/100") == 0
    assert convert("1/100") == 1
    assert convert("100/100") == 100
    assert convert("99/100") == 99


def test_gauge():
    assert gauge(33) == "33%"
    assert gauge(75) == "75%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("one/two")
