from flask import Flask, abort, request
app = Flask(__name__)
import requests
import xmltodict as xd
import json

XML_CURRENCY_EXCHANGE_RATE = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml"
currencies = {}

def load_exchange_rates(url):
    ''' load data from url '''

    def _load_from_url():
        ''' load from url '''
        return xd.parse(requests.get(url).text)
    
    def _load_from_file():
        ''' used for testing purpose '''
        with open(url,'r') as f:
            return xd.parse(f.read())
        
    if url.find("https://") != -1:
        print("loading from url")
        data = _load_from_url()
    else:
        print("loading from file")
        data = _load_from_file()

    for c in data["gesmes:Envelope"]["Cube"]["Cube"]:
        time = c["@time"]
        for item in c["Cube"]:
            if not time in currencies:
                currencies[time] = {}
            currencies[time][item["@currency"]] = item["@rate"]
    return currencies


@app.route("/calc_exchange/", methods=['POST'])
def calc_exchange(data = None):
    if not data:
        data = request.json
    reference_date = data["reference_date"]
    currency_src = data["src_currency"]
    currency_dest = data["dest_currency"]
    amount = data["amount"]

    if not reference_date in currencies:
        return json.dumps({"message": "Error date not found!"})
    
    currency_src = currency_src.upper()
    currency_dest = currency_dest.upper()
    if currency_src != "EUR":
        rate_src = currencies[reference_date][currency_src]
        conv = amount / float(rate_src)
    else:
        # if eur -> another
        rate_dest = currencies[reference_date][currency_dest]
        conv = amount * float(rate_dest)
    
    return json.dumps({'amount': conv, 'currency':currency_dest})
    
if __name__ == '__main__':
    load_exchange_rates(XML_CURRENCY_EXCHANGE_RATE)
    app.run(host='0.0.0.0', port=5000, debug=True)

    # test:
    #load_exchange_rates("data/eurofxref-hist-90d.xml")
    #print ( json.loads( calc_exchange({"amount": 1, "src_currency": "EUR", "dest_currency": "USD", "reference_date": "2018-07-02"}) )["amount"]  )

    

