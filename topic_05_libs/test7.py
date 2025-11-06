
import requests

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

#print(response.json())

for elem in response.json():
    if (elem["cc"] == "EUR" or elem["cc"] == "USD"):
        print(elem)