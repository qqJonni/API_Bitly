import os
from dotenv import load_dotenv, find_dotenv
import requests


def start():
    load_dotenv(find_dotenv())
    token = os.environ.get('BITLY_TOKEN')
    headers = {'Authorization': token}
    response = requests.get('https://api-ssl.bitly.com/v4/user', headers=headers)
    print(response.json())


if __name__ == '__main__':
    start()
