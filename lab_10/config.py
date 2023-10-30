import os

base_dir = os.path.abspath(os.path.dirname(__file__))

images_dir = os.path.join(base_dir, 'images')
background_path = os.path.join(images_dir, 'background.jpg')

model_dir = os.path.join(base_dir, 'vosk-model')

voice = 'english'
