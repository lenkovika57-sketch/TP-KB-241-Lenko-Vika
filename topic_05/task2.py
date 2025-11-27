import requests

currency_list = ["USD", "EUR", "PLN"]

currency = input("Введіть тип валюти (USD, EUR, PLN): ").upper()

if currency not in currency_list:
    print("Помилка! Невідома валюта.")
else:
    amount = float(input("Введіть кількість валюти: "))

    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency}&json"
    response = requests.get(url).json()

    rate = response[0]["rate"]
    result = amount * rate

    print(f"Курс {currency}: {rate} грн")
    print(f"{amount} {currency} = {result:.2f} грн")