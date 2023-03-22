import requests
import time
import argparse
from playsound import playsound


def get_bitcoin_price(currency='USD'):
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    response_json = response.json()
    current_price = response_json['bpi'][currency]['rate']
    return float(current_price.replace(',', ''))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-C', '--currency', type=str, default='USD',
                        help='Currency to check the price. (Default: USD)')
    parser.add_argument('-M', '--min', type=float, default='30000',
                        help='Minimum price to alert. (Default: 30000)')
    parser.add_argument('-T', '--time', type=float, default='10',
                        help='Time in seconds to check the price. (Default: 10)')

    args = parser.parse_args()

    while True:
        if get_bitcoin_price(args.currency) < args.min:
            playsound('./you-suffer.mp3')

        time.sleep(args.time)
