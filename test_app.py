from app import * 
import json 


# load from file for speedup tests
load_exchange_rates("data/eurofxref-hist-90d.xml")


def test_conversions():
    assert json.loads(calc_exchange({"amount": 1, "src_currency": "EUR", "dest_currency": "USD", "reference_date": "2018-07-02"}))["amount"] == 1.1639
    assert json.loads(calc_exchange({"amount": 1, "src_currency": "EUR", "dest_currency": "GBP", "reference_date": "2018-07-02"}))["amount"] == 0.8865
    assert json.loads(calc_exchange({"amount": 1, "src_currency": "GBP", "dest_currency": "EUR", "reference_date": "2018-07-02"}))["amount"] == 1.1280315848843767
    assert json.loads(calc_exchange({"amount": 10, "src_currency": "GBP", "dest_currency": "EUR", "reference_date": "2018-07-02"}))["amount"] == 11.280315848843768
    assert json.loads(calc_exchange({"amount": 10, "src_currency": "EUR", "dest_currency": "USD", "reference_date": "2018-07-02"}))["amount"] == 11.639

def test_date_null():
    assert json.loads(calc_exchange({"amount": 1, "src_currency": "EUR", "dest_currency": "USD", "reference_date": None}))["message"] == "Error date not found!"
    
def test_date_invalid():    
    assert json.loads(calc_exchange({"amount": 1, "src_currency": "EUR", "dest_currency": "USD", "reference_date": "2030-01-01"}))["message"] == "Error date not found!"
