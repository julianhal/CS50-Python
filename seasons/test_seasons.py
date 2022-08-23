# Unit tests of my solution to https://cs50.harvard.edu/python/2022/psets/8/seasons/

import pytest, sys
from seasons import convert, get_date
from datetime import date


def test_get_date():
    assert get_date("2021-08-02") == (2021, 8, 2)


def test_convert():
    assert (
        convert(date(2021, 8, 2))
        == "Five hundred twenty-five thousand, six hundred minutes"
    )
    assert (
        convert(date(2020, 8, 2))
        == "One million, fifty-one thousand, two hundred minutes"
    )


def test_exit():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        try:
            year, month, day = get_date("Febrary 6th 2001")
            birth = date(year, month, day)
        except (ValueError, TypeError):
            sys.exit("Not a valid date!")
    assert pytest_wrapped_e.type == SystemExit
