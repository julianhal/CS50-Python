# Solution to https://cs50.harvard.edu/python/2022/psets/6/shirt/

import sys, os
from PIL import Image, ImageOps

# Validate command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments!")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments!")

# Validate correct extensions on the files
name, ext_1 = os.path.splitext(sys.argv[1])
name, ext_2 = os.path.splitext(sys.argv[2])
valid_ext = [".jpg", ".png", ".jpeg"]
if ext_1 not in valid_ext or ext_2 not in valid_ext:
    sys.exit("Not valid files!")
elif ext_1 != ext_2:
    sys.exit("File extensions do not match!")

# Open shirt file and as input
try:
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    sys.exit("Could not find shirt to overlay image!")
try:
    img = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit(f"Could not find {sys.argv[1]}!")

# resize and crop the input
img_cropped = ImageOps.fit(img, shirt.size)

# overlay the shirt
img_cropped.paste(shirt, shirt)

# save the result
img_cropped.save(sys.argv[2])
