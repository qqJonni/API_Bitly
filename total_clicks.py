from dotenv import load_dotenv, find_dotenv
import requests


def count_clicks(token, bitlink):
    load_dotenv(find_dotenv())

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary', headers=headers)
    total_clicks = response.json().get('total_clicks')

    return total_clicks


if __name__ == '__main__':
    try:
        clicks_count = count_clicks(input('Enter token: '), input('Enter bitlink: '))
    except requests.exceptions.HTTPError as e:
        print(f'HTTP Error occurred: {str(e)}')
    else:
        print(f'Summary cliks: {clicks_count}')
