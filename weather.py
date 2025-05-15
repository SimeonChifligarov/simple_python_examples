import requests

city = input("Въведи име на град: ")
url = f"https://wttr.in/{city}?format=3"

response = requests.get(url)
print("Прогноза за времето:", response.text)
