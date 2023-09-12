"""
#ejemplo de una API local con puerto 3501 y dentro de un /api
from flask import Flask
app = Flask(__name__)

@app.route('/api/')
def api():
    return 'Hello, API!'

if __name__ == "__main__":

    app.run(host="0.0.0.0",port = 3501, debug=True)

"""
from urllib import request

#ejemplo de una API local con puerto 3501 y dentro de un /api
from flask import Flask
from yahoo_funcion_data import get_price
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/api/<ticker>")


#def api():
    #return {"ticker":"DIS", "precio": 5001,"currency": "USD"}
    #return get_price("DIS")

#def api(ticker):
#    return (get_price(ticker)

@app.route("/api/multiple/")

def api_multiple():
    tickers = request.args.get('tickers')
    tickers = tickers.split(',') #split separa x el tipo de caracter entre comillas  contrario es '--'.joing

    result = []
    for t in tickers:
        result.append(get_price(t))
    return result

@app.route("/api/<ticker>", methods=["GET"])
def get_ticker(ticker: object) -> object:
    return get_price(ticker)


@app.route("/api/<ticker>", methods=["POST"])
def post_ticker(ticker):
    document = get_price(ticker)
    return set_price(document)


@app.route("/api/multiple/")
def api_multiple():
    tickers = request.args.get('tickers')
    tickers = tickers.split(',')

    result = []
    for t in tickers:
        result.append(get_price(t))
    return result



if __name__ == "__main__":

    app.run(host="0.0.0.0",port = 3501, debug=True)
