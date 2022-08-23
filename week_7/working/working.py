# Solution to https://cs50.harvard.edu/python/2022/psets/7/working/

import re


def main():
    print(convert(input("Hours: ")))


def check_time(hour_1, min_1, hour_2, min_2):
    if int(hour_1) not in range(13) or int(hour_2) not in range(13):
        raise ValueError
    if min_1 != "":
        if int(min_1) not in range(60):
            raise ValueError
    if min_2 != "":
        if int(min_2) not in range(60):
            raise ValueError


def convert(s):
    if matches := re.search(
        r"(\d\d?):?(\d?\d?) ((?:A|P)M) to (\d\d?):?(\d?\d?) ((?:A|P)M)", s
    ):
        hour_1, min_1, p1, hour_2, min_2, p2 = matches.groups()
        check_time(hour_1, min_1, hour_2, min_2)

        # Check each prefix for AM or PM, then convert the hours and minutes to 24-hour format
        if p1 == "AM":
            hour_1 = 0 if int(hour_1) == 12 else int(hour_1)
        else:
            hour_1 = 12 if int(hour_1) == 12 else int(hour_1) + 12
        if p2 == "AM":
            hour_2 = 0 if int(hour_2) == 12 else int(hour_2)
        else:
            hour_2 = 12 if int(hour_2) == 12 else int(hour_2) + 12
        if min_1 == "":
            min_1 = "00"
        if min_2 == "":
            min_2 = "00"
        return f"{hour_1:02}:{min_1} to {hour_2:02}:{min_2}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
