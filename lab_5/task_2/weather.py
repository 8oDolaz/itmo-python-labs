from weather_api import WeatherAPI

def main():
    api = WeatherAPI(API_key)
    api.set_city(city)

    weather = api.weather()

    output = f'Сейчас на улице довольно {"холодно" if weather["temp"] < 13 else "тепло"}, температура {weather["temp"]} градусов цельсия. '
    output += f'Ощущается как {weather["feels_like"]}.\n'
    output += f'Давление составляет {weather["pressure"]} миллиметров ртутного столба\n'
    output += f'Влажность {"высокая" if weather["humidity"] > 70 else "низкая"}: {weather["humidity"]}%'

    print(output)

if __name__ == '__main__':
    API_key = open('weather_api_key.txt').read()
    city = 'Saint-Petersburg'

    main()
