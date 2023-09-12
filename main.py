"""
#un valor de una empresa con agente y extracci[on de datos

import requests
#url="https://query1.finance.yahoo.com/v8/finance/chart/KO?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance"
ticker = "DIS"
url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
print (url)

user_agent = {'User-agent':'Mozilla/5.0'}
print (user_agent)
#a = requests.get(url).content
#print(a)

r = requests.get(url=url, headers=user_agent).json()
print(r)

precio= r['chart']['result'][0]['meta']['regularMarketPrice']
currency= r['chart']['result'][0]['meta']['currency']

print(f"{ticker}:{precio} {currency}")

"""
#################################################################
"""
#varios valores de retorno de varias empresas

import requests

tickers = ["DIS", "KO" ,"PEP", "F", "V"]

for ticker in tickers:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    user_agent = {'User-agent':'Mozilla/5.0'}

    r = requests.get(url=url, headers=user_agent).json()
    #print(r)

    precio= r['chart']['result'][0]['meta']['regularMarketPrice']
    currency= r['chart']['result'][0]['meta']['currency']
    print(f"{ticker}:{precio} {currency}")

"""


#################################################################



#en funcion para impresion de datos

#import requests
from yahoo_funcion_data import get_price
tickers = ["DIS", "KO" ,"PEP", "F", "V"]
"""
def get_price(ticker: str, verbose: bool = False) -> float: #no es necesario poner los tipo de caracter
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    user_agent = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(url=url, headers=user_agent).json()

    precio = r['chart']['result'][0]['meta']['regularMarketPrice']
    currency = r['chart']['result'][0]['meta']['currency']

    if verbose:
        print(f"{ticker}:{precio} {currency}")
    return precio
"""
for t in tickers:
    get_price(ticker=t,verbose=True)


