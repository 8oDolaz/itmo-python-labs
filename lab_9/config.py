import os

app_name = 'Notes'

base_dir = os.path.abspath(os.path.dirname(__file__))

secret_key = open(os.path.join(base_dir, 'secret_key.txt'), 'r').read()
database_uri = 'sqlite:///' + os.path.join(base_dir, 'database.db')

default_note_title = 'Без названия'
