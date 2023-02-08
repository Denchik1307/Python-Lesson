import requests

params = {'q': "Minsk", 'units': 'metric', 'lang': 'en', 'APPID': 'fae5dd0f62a12ec7711587ceb88bc717'}


def get_weather(city: str):
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

        city_name = in_data['name']

        main = in_data['main']
        pressure = main['pressure']
        temperature = main['temp']
        max_temperature = main['temp_max']
        min_temperature = main['temp_min']
        humidity = main['humidity']

        wind = in_data['wind']
        wind_speed = wind['speed']
        direction_deg = wind['deg']
        direction = calc_direction(direction_deg)

        coordinate = in_data['coord']
        lon = coordinate['lon']
        lat = coordinate['lat']
        weather_ten_days = f"https://yandex.by/pogoda/details/10-day-weather?lat={lat}&lon={lon}&via=ms"

        return f"Weather in {city_name}:\n" \
               f"Pressure -> {pressure} мм.рт. ст\n" \
               f"Temperature -> {temperature}°С " \
               f"({max_temperature}↑ | {min_temperature}↓) \n" \
               f"Humidity -> {humidity} %\n" \
               f"Wind -> {wind_speed} m/s\n" \
               f"Direction -> {direction} \n" \
               f"\nLocation on map:\n" \
               f"Longitude {lon}\n" \
               f"Latitude {lat}\n" \
               f"{weather_ten_days}"

    params['q'] = city.lower().capitalize()
    try:
        url_weather_api = "https://api.openweathermap.org/data/2.5/weather"
        response = requests.get(url_weather_api, params=params)
        data = response.json()
        return make_result(data)
    except Exception as err:
        print(err)
        return f"I can`t find this city \"{city}\" 🤔"

