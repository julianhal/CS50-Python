# Solution to https://cs50.harvard.edu/python/2022/psets/5/test_bank/

from bank import value


def test_start():
    assert value("hello") == 0
    assert value("hello   ") == 0
    assert value("HEllO   ") == 0
    assert value("hello, how are you!!!?? .,<>") == 0


def test_hello():
    assert value("How are you doin?") == 20
    assert value("how are you doin?") == 20


def test_random():
    assert value("   RandOM TEXT 22334  ") == 100
