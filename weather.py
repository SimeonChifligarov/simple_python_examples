import requests

city = input("Въведи име на град: ")
url = f"https://wttr.in/{city}"

response = requests.get(url)
print("Прогноза за времето:", response.text)
