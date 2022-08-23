# Unit tests of my solution to https://cs50.harvard.edu/python/2022/psets/7/numb3rs/

from numb3rs import validate


def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
    assert validate("1.2.3.1000") == False
    assert validate("512.512.512.512") == False
    assert validate("cat") == False
    assert validate("1.0.256.1") == False
