# Solution to https://cs50.harvard.edu/python/2022/psets/7/watch/

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(
        r'<iframe .*?src="https?:\/\/w?w?w?\.?youtube\.com\/embed\/(.+?)".+<\/iframe>',
        s,
    ):
        return f"https://youtu.be/{matches.group(1)}"


if __name__ == "__main__":
    main()
