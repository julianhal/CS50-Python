# Solution to https://cs50.harvard.edu/python/2022/psets/3/outdated/

import sys


def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    # Create enumerated dictionary
    date_dict = dict(
        i for i in enumerate(months, start=1)
    )  # Ref learning material: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

    # Get input from user
    while True:
        date = input("Date: ").strip()
        if date[0].isnumeric():
            try:
                month, day, year = date.split("/")
            except ValueError:
                pass
            else:
                # Do something with date = [month, day, year]
                if 0 < int(month) <= 12 and 0 < int(day) <= 31 and len(year) == 4:
                    print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
                    sys.exit()
        else:
            try:
                month, day, year = date.split(" ")
            except ValueError:
                pass
            else:
                if (
                    month in months
                    and 0 < int(day.rstrip(",")) <= 31
                    and len(year) == 4
                    and not day.isnumeric()
                ):
                    new_month = int(months.index(month)) + 1
                    print(f"{year}-{new_month:02}-{int(day.rstrip(',')):02}")
                    sys.exit()


if __name__ == "__main__":
    main()
