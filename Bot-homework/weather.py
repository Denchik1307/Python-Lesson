import requests

params = {'q': "Minsk", 'units': 'metric', 'lang': 'en', 'APPID': 'fae5dd0f62a12ec7711587ceb88bc717'}


def get_weather(city: str):
    params['q'] = city.lower().capitalize()
    print(params)
    try:
        response = requests.get("http://api.openweathermap.org/data/2.5/weather",
                                params=params)
        data = response.json()
        print(data)

        return make_result(data)
    except Exception as err:
        return f"Can`t find this city \"{city}\" 🤔"


def make_result(in_data):
    return f"In {in_data['name']}:\n" \
           f"Pressure -> {in_data['main']['pressure']} Kpa\n" \
           f"Temperature -> {in_data['main']['temp']} °С\n" \
           f"Humidity -> {in_data['main']['humidity']} %\n" \
           f"Wind -> {in_data['wind']['speed']} m/s\n"  # print(weather)
