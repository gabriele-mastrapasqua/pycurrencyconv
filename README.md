# python currency converter

this is a simple flask REST API that convert the provided amount​ from src_currency​ to dest_currency​,
given the exchange rate at the reference_date​.

The request is done calling: 

POST http://localhost:5000/calc_exchange/

the request body is like this:


curl -X POST -H "Content-Type: application/json" -d '{"amount": 12.35, "src_currency": "EUR", "dest_currency": "USD", "reference_date": "2018-07-02"}' http://localhost:5000/calc_exchange/


The response is a JSON object like this:
{"amount": 14.374165, "currency": "USD"}



There is an xml file with the last 90 days exchange rates at this link:
- https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml


## install

virtualenv env
source env/bin/activate

pip3 install flask
pip3 install requests

## to run

export LC_ALL=C.UTF-8
export LANG=C.UTF-8
FLASK_APP=app.py flask run

## to test

pytest

