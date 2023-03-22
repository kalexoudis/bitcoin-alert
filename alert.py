import requests
import time
from playsound import playsound


def get_bitcoin_price(currency='USD'):
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    response_json = response.json()
    current_price = response_json['bpi'][currency]['rate']
    return float(current_price.replace(',', ''))


if __name__ == '__main__':
    while True:
        print(get_bitcoin_price())
        if get_bitcoin_price() < 30000:
            playsound('./you-suffer.mp3')
            time.sleep(10)
