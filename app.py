import requests
city = input("Enter city name:")
api_Key = "0fc1ec170f3011650c75139d5d705a1c"
url =
f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_Key}&units=metric"
data = requests.get(url).json()
if data.get("main"):
      print("Tewmperature:", data["main"]
      ["temp"])
      print("Weather:", data["weather"][0]
      ["description"])
else:
      print("Errot:", data)
