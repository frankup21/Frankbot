import requests

def getprice():
    data = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json').json()
    price = data['bpi']['USD']['rate']
    return price
