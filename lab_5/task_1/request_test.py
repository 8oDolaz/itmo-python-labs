import requests

if __name__ == '__main':
    url = 'https://hh.ru/?hhtmFrom=main'

    response = requests.get(
        url, headers={
            'User-Agent': 'Custom'
        }
    )

    with open('response.html', 'w') as html:
        html.write(response.text)
