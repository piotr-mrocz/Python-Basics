import requests

base = "PLN"
response = requests.get("https://api.exchangeratesapi.io/latest?base=" + base)

if (response.ok):
    data = response.json()
    rates = data["rates"]
    base = data["base"]
    date = data["date"]


for key in rates:
    print(f"{key}: {rates[key]}")