import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(
        "https://rest.coincap.io/v3/price/bysymbol/BTC"
    )
    data = response.json()

    price = float(data['data']["priceUsd"])

except requests.RequestException:
    sys.exit("Request failed")

amount = n * price

print(f"${amount:,.4f}")