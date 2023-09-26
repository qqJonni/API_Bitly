import os
from dotenv import load_dotenv, find_dotenv
import requests


def shorten_link(token, url):
    load_dotenv(find_dotenv())

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    data = f'{{ "long_url": "{url}" }}'
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, data=data)

    if response.status_code == 200:
        bitlink = response.json().get('link')
        print(f'Битлинк: {bitlink}')
    else:
        print('Error occurred.')


if __name__ == '__main__':
    shorten_link(input('Enter token: '), input('Enter url: '))
