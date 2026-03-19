import requests
city = input("Enter city name:")
api_Key = "your_api_Key_here"
url =
f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_Key}&units=metric"
data = requests.get(url).json()
print("Tewmperature:", data["main"]
      ["temp"])
print("Weather:", data["weather"][0]
      ["description"])
