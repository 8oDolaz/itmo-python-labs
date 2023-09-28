import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.__api_key = api_key
        self.__base_url = 'http://api.openweathermap.org'

        self.units = 'metric'

    def __add_url_params(self, url: str, params: dict) -> str:
        url = f'{url}?' + "&".join(f'{key}={val}' for key, val in params.items())
        url += f'&appid={self.__api_key}'

        return url

    def set_city(self, city_name: str) -> None:
        request_params = {
            'q': city_name,
        }

        url = self.__add_url_params(f'{self.__base_url}/geo/1.0/direct', request_params)

        response = requests.get(url)
        response = response.json()[0]

        self.city_name = response['name']
        self.city_lat = response['lat']
        self.city_lon = response['lon']

    def weather(self) -> dict:
        request_params = {
            'lat': self.city_lat,
            'lon': self.city_lon,
            'units': self.units
        }

        url = self.__add_url_params(f'{self.__base_url}/data/2.5/forecast', request_params)

        response = requests.get(url)
        response = response.json()['list'][0]['main']

        return response
