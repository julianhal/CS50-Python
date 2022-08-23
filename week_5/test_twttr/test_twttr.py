# Solution to https://cs50.harvard.edu/python/2022/psets/5/test_twttr/

from twttr import shorten


def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
    assert shorten("AEIOU") == ""
