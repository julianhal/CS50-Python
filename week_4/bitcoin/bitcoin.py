# Solution to https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import sys
import requests

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number!")
except IndexError:
    sys.exit("Usage: './bitcoin.py n-bitcoins'")
else:
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Couldn't get price of bitcoin")
    else:
        o = r.json()
        USD = n * o["bpi"]["USD"]["rate_float"]
        print(f"${USD:,.4f}")
