import requests

params = {'q': "Minsk", 'units': 'metric', 'lang': 'en', 'APPID': 'fae5dd0f62a12ec7711587ceb88bc717'}


def get_weather(city: str):
    params['q'] = city.lower().capitalize()
    print(params)
    try:
        response = requests.get("https://api.openweathermap.org/data/2.5/weather",
                                params=params)
        data = response.json()
        return make_result(data)
    except Exception as err:
        print(err)
        return f"Can`t find this city \"{city}\" 🤔"


def calc_direction(direction_deg):
    tmp = ""
    if 23 <= direction_deg < 67:
        tmp = "NE"
    elif 67 <= direction_deg < 113:
        tmp = "E"
    elif 113 <= direction_deg < 157:
        tmp = "SE"
    elif 157 <= direction_deg < 203:
        tmp = "S"
    elif 203 <= direction_deg < 247:
        tmp = "SW"
    elif 247 <= direction_deg < 293:
        tmp = "W"
    elif 293 <= direction_deg < 337:
        tmp = "NW"
    else:
        tmp = "N"
    return tmp


def make_result(in_data):
    direction_deg = in_data['wind']['deg']
    direction = calc_direction(direction_deg)
    return f"In {in_data['name']}:\n" \
           f"Pressure -> {in_data['main']['pressure']} Kpa\n" \
           f"Temperature -> {in_data['main']['temp']} °С\n" \
           f"Humidity -> {in_data['main']['humidity']} %\n" \
           f"Wind -> {in_data['wind']['speed']} m/s\n" \
           f"Direction -> {direction} \n"
