# Solution to https://cs50.harvard.edu/python/2022/psets/2/nutrition/


def main():
    pairs = create_dict()
    print(pairs)
    food = input("Input: ")
    if food.title() in pairs:
        print("Calories:", pairs[food.title()])


def create_dict():
    table = """Apple	130
    1 large
    (242 g/
    8 oz)
    Avocado	50
    1/5 medium
    (30 g/
    1.1 oz)
    Banana	110
    1 medium
    (126 g/
    4.5 oz)
    Cantaloupe	50
    1/4 medium
    (134 g/
    4.8 oz)
    Grapefruit	60
    1/2 medium
    (154 g/
    5.5 oz)
    Grapes	90
    3/4 cup
    (126 g/
    4.5 oz)
    Honeydew 	50
    Melon
    1/10 medium
    4.8 oz)
    Kiwifruit	90
    2 medium
    (148 g/
    5.3 oz)
    Lemon	15
    1 medium
    (58 g/
    2.1 oz)
    Lime	20
    1 medium
    (67 g/
    2.4 oz)
    Nectarine	60
    1 medium
    (140 g/
    5.0 oz)
    Orange	80
    1 medium
    (154 g/
    5.5 oz)
    Peach	60
    1 medium
    (147 g/
    5.3 oz)
    Pear	100
    1 medium
    (166 g/
    5.9 oz)
    Pineapple	50
    2 slices,
    3/4" thick
    (112 g/4 oz)
    Plums	70
    2 medium
    (151 g/
    5.4 oz)
    Strawberries	50
    8 medium
    (147 g/
    5.3 oz)
    Sweet Cherries	100
    21 ;
    1 cup
    5.0 oz)
    Tangerine	50
    1 medium
    (109 g/
    3.9 oz)
    Watermelon	80
    """
    # Create list of foods
    tmp = ""
    for line in table.split("\n")[::4]:
        tmp += line + "\n"

    list = tmp.split("\n")
    list.pop()

    # Remove whitespace from dict
    # List compehension article: https://www.programiz.com/python-programming/list-comprehension
    list = [i.strip() for i in list]

    print(list)

    # Create dictionary of foods
    result = {}
    for item in list:
        key, val = item.split("\t")
        result[key] = val
    return result


if __name__ == "__main__":
    main()
