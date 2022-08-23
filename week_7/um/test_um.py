# Unit tests of my solution to https://cs50.harvard.edu/python/2022/psets/7/um/

from um import count


def test_convert():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
