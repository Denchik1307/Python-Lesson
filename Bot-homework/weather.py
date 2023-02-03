import requests
import emoji


params = {'q': "Minsk", 'units': 'metric', 'lang': 'en', 'APPID': 'fae5dd0f62a12ec7711587ceb88bc717'}


def get_weather(city: str):
    params['q'] = city.lower().capitalize()
    print(params)
    try:
        responce = requests.get("http://api.openweathermap.org/data/2.5/weather",
                                params=params)
        data = responce.json()
        # print(data)
        weather = f"In {params['q']}:\n" \
                  f"Temp -> {data['name']} °С\n" \
                  f"Pressure -> {data['main']['pressure']} Kpa\n" \
                  f"Humidity -> {data['main']['humidity']} %\n" \
                  f"Wind -> {data['wind']['speed']} m/s\n"  # print(weather)
        return weather
    except Exception as err:
        return f"Can`t find this city \"{city}\" 🤔"
