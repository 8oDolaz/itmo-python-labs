import os
import requests

import config


class DogAPI:
    def __init__(self) -> None:
        self._base_url = 'https://dog.ceo/api/breeds/image/random'

        self._id = None
        self.url = None
        self.breed = None

    def __repr__(self) -> str:
        return f'(url: {self.url}, breed: {self.breed})'

    def save_image(self, background = False) -> None:
        if self._id is None:
            raise ValueError("You don't have an image currently. Please run next() method.")

        response_image = requests.get(self.url)

        if response_image.status_code != 200:
            raise RuntimeError("Couldn't download image")

        if background:
            image_path = os.path.join(config.images_dir, f'background.jpg')
        else:
            image_path = '_'.join(self.breed.split())
            image_path = os.path.join(config.images_dir, f'{image_path}_{self._id}.jpg')

        with open(image_path, 'wb') as image:
            image.write(response_image.content)

    def next(self) -> None:
        response_json = requests.get(self._base_url)

        if response_json.status_code != 200:
            raise RuntimeError("Something went wrong.")

        response_json = response_json.json()
        self.url = response_json['message']

        url_components = self.url.split('/')
        self.breed = url_components[-2]
        self.breed = ' '.join(self.breed.split('-'))
        self._id = url_components[-1].split('.')[-2]
