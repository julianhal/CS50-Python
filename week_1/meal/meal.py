# Solution to https://cs50.harvard.edu/python/2022/psets/1/meal/
def main():
    time = input("What time is it? ")
    x = convert(time)
    if 7 <= x <= 8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")


def convert(time):
    hours, min = time.split(":")
    return float(hours) + float(min) / 60


if __name__ == "__main__":
    main()
