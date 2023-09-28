import requests

class RnMApi:
    def __init__(self):
        self.__base_url = 'https://rickandmortyapi.com/api'

        self.episodes_kwargs = {'name': [str]}

    @staticmethod
    def __add_kwargs(url, **kwargs) -> str:
        return url + '?' + '&'.join(f'{key}={val}' for key, val in kwargs.items())

    def __character_info(self, url: str) -> dict:
        response = requests.get(url).json()
        filtered_response = {
            key: response[key]
            for key in ['id', 'name', 'species']
        }

        return filtered_response

    def series_info(self) -> dict:
        url = f'{self.__base_url}/episode'

        response = requests.get(url).json()

        stats = {
            'total_episodes': response['info']['count'],
            'first_episode': response['results'][0]['air_date'],
        }

        return stats

    def find_episode(self, **kwargs) -> dict:
        for param in kwargs:
            if not (param in self.episodes_kwargs):
                supported_args = ", ".join(f"{key}: {val}" for key, val in self.episodes_kwargs)
                raise KeyError(f'Supported arguments are: {supported_args}')

            if not (type(kwargs[param]) in self.episodes_kwargs[param]):
                raise TypeError(f'Unsupported type for "{param}" argument, should be {self.episodes_kwargs[param]}')

        url = f'{self.__base_url}/episode'
        url = self.__add_kwargs(url, **kwargs)

        response = requests.get(url).json()

        episode = response['results'][0]
        episode['characters'] = [
            self.__character_info(link)
            for link in episode['characters'][:5]
        ]

        return episode
