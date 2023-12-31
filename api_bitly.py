import requests
from dotenv import load_dotenv, find_dotenv
import os
import argparse


def shorten_link(token, url):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    payload = {
        'long_url': url
    }
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=payload)
    response.raise_for_status()
    bitlink = response.json()['link']
    return bitlink


def count_clicks(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary', headers=headers)
    response.raise_for_status()
    total_clicks = response.json()['total_clicks']
    return total_clicks


def is_bitlink(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}', headers=headers)
    response_check = response.ok

    return response_check


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    token = os.environ['BITLY_TOKEN']
    parser = argparse.ArgumentParser('Эта программа преобразует длинные url ссылки в короткие')
    parser.add_argument('url', help='Enter url')
    args = parser.parse_args()

    if is_bitlink(token, args.url):
        clicks_count = count_clicks(token, args.url)
        print(f'Total Clicks: {clicks_count}')
    else:
        bitlink = shorten_link(token, args.url)
        print(f'Shortened Bitlink: {bitlink}')
