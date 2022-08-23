# Solution to https://cs50.harvard.edu/python/2022/psets/7/numb3rs/

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Checks if the ip is in the following format #.#.#.#
    matches = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)

    # List comprehensions and all() to check if ip numbers are betwen 0-255
    try:
        return all(int(number) in range(256) for number in matches.groups())
    except AttributeError:
        return False


if __name__ == "__main__":
    main()
