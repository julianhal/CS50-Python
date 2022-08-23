# Solution to https://cs50.harvard.edu/python/2022/psets/5/test_plates/

from plates import is_valid


def test_length():
    assert is_valid("CSGOKJKJLKJ") == False
    assert is_valid("C") == False


def test_char():
    assert is_valid("aa. !") == False


def test_numbers():
    assert is_valid("88GO") == False
    assert is_valid("88888") == False
    assert is_valid("CS69GO") == False
    assert is_valid("CS05") == False


def test_correct():
    assert is_valid("CS50") == True
