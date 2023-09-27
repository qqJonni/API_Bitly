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
    bitlink = response.json().get('link')

    return bitlink


if __name__ == '__main__':
    try:
        bitlink = shorten_link(input('Enter token: '), input('Enter url: '))
    except requests.exceptions.HTTPError as e:
        print(f'HTTP Error occurred: {str(e)}')
    else:
        print(f'Битлинк: {bitlink}')
