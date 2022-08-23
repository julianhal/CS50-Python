# Solution to https://cs50.harvard.edu/python/2022/psets/7/um/

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if matches := re.findall(r"\bum\b", s, re.IGNORECASE):
        return len(matches)


if __name__ == "__main__":
    main()
