import  requests

city= "Moscow,RU"
appid = "961174bd180d9b05fefa1edc52f98486"

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
    params={'q': city,'units':'metric','lang':'ru','APPID': appid})
data = res.json()
print('прогноз погоды на неделю')
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература<",
          '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",
          i['weather'][0]['description'], ">")
    print('_______________________')