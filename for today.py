import requests

city= "Moscow,RU"
appid = "961174bd180d9b05fefa1edc52f98486"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                  params={'q': city, 'units': 'metric', 'lang':'ru', 'APPID': appid})
data = res.json()

print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Скорость ветра: ", data["wind"]["speed"])
print("Видимость: ", data["visibility"])
