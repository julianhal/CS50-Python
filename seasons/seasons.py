# Solution to https://cs50.harvard.edu/python/2022/psets/8/seasons/

import re, sys, inflect
from datetime import date


def main():
    # Promt user for date of birth
    try:
        year, month, day = get_date(input("Date of birth: "))
        birth = date(year, month, day)
    except (ValueError, TypeError):
        sys.exit("Not a valid date!")

    # Calculate how old they are in minuttes and print that in a sentence
    print(convert(birth))


# Get a valid date from user and return it
def get_date(date):
    if matches := re.search(r"^(\d\d\d\d)-(\d\d)-(\d\d)$", date):
        return int(matches.group(1)), int(matches.group(2)), int(matches.group(3))


# Converts date to minutes in word phrase
def convert(birth):
    duration = date.today() - birth
    min = duration.total_seconds() / 60
    p = inflect.engine()
    return f'{p.number_to_words(int(min), andword="").capitalize()} minutes'


if __name__ == "__main__":
    main()
