import os
from dotenv import load_dotenv, find_dotenv
import requests


def start():
    load_dotenv(find_dotenv())
    token = os.environ.get('BITLY_TOKEN')
    long_url = 'http://dvmn.org'

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    data = f'{{ "long_url": "{long_url}" }}'
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, data=data)

    print(response.json())


if __name__ == '__main__':
    start()
