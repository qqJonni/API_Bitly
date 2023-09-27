from dotenv import load_dotenv, find_dotenv
import requests
from urllib.parse import urlparse


def shorten_link(token, url):
    load_dotenv(find_dotenv())

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    data = f'{{ "long_url": "{url}" }}'
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, data=data)
    bitlink = response.json().get('link')

    return bitlink


def count_clicks(token, bitlink):
    load_dotenv(find_dotenv())

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary', headers=headers)
    total_clicks = response.status_code

    return total_clicks


def is_bitlink(url):
    parsed = urlparse(url)
    if parsed.netloc == 'bit.ly':
        try:
            clicks_count = count_clicks(input('Enter token: '), url)
        except requests.exceptions.HTTPError as e:
            print(f'HTTP Error occurred: {str(e)}')
        else:
            print(f'Summary cliks: {clicks_count}')
    else:
        try:
            bitlink = shorten_link(input('Enter token: '), url)
        except requests.exceptions.HTTPError as e:
            print(f'HTTP Error occurred: {str(e)}')
        else:
            print(f'Битлинк: {bitlink}')


if __name__ == '__main__':
    is_bitlink(input('Enter url: '))
