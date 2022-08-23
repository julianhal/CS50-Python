# Solution to https://cs50.harvard.edu/python/2022/psets/2/plates/


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_characters(s) and check_lenth(s) and check_numbers(s):
        return True


def check_lenth(s):
    # least 2 max 6 characters
    if not 2 <= len(s) <= 6:
        return False

    # minimum 2 characters
    count = 0
    for i in s:
        if i.isalpha():
            count += 1
    if count < 2:
        return False
    return True


def check_numbers(s):
    # check if numbers startwith 0
    for i in s:
        if i.isnumeric():
            if int(i) == 0:
                return False
            break

    # Check if all the numbers are at the end of str
    for i in s:
        if i.isnumeric():
            # check rest of string for alphabetic
            for j in s[s.find(i) :]:
                if j.isalpha():
                    return False
    return True


def check_characters(s):
    if not s.isalnum():
        return False
    return True


if __name__ == "__main__":
    main()
