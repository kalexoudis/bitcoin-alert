import requests


def get_bitcoin_price(currency='USD'):
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    response_json = response.json()
    current_price = response_json['bpi'][currency]['rate']
    return current_price


if __name__ == '__main__':
    print(get_bitcoin_price())
