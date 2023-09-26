import os
from dotenv import load_dotenv, find_dotenv


def start():
    load_dotenv(find_dotenv())
    token = os.environ.get('BITLY_TOKEN')


if __name__ == '__main__':
    start()
