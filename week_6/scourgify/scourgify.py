# Solution to https://cs50.harvard.edu/python/2022/psets/6/scourgify/

import sys, csv

# Validate user input
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments!")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments!")

# Read old csv into a list of dictionary values
new_dicts = []
try:
    with open(sys.argv[1], "r") as old_csv:
        reader = csv.DictReader(old_csv)
        for row in reader:
            last, first = row["name"].split(",")
            first = first.strip()
            house = row["house"]
            new_dicts.append({"first": first, "last": last, "house": house})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}!")

# Write list of dictionaries to new csv file
with open(sys.argv[2], "w") as new_csv:
    writer = csv.DictWriter(new_csv, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in new_dicts:
        writer.writerow(row)
