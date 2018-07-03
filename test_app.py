from app import * 
import json 


# load from file for speedup tests
load_exchange_rates("data/eurofxref-hist-90d.xml")


def test_conversions():
    assert calc_exchange(1, "EUR", "USD", "2018-07-02")["amount"] == 1.1639
    assert calc_exchange(1, "EUR", "GBP", "2018-07-02")["amount"] == 0.8865
    assert calc_exchange(1, "GBP", "EUR", "2018-07-02")["amount"] == 1.1280315848843767
    assert calc_exchange(10, "GBP", "EUR", "2018-07-02")["amount"] == 11.280315848843768
    assert calc_exchange(10, "EUR", "USD", "2018-07-02")["amount"] == 11.639

def test_date_null():
    assert calc_exchange(10, "EUR", "USD", None)["message"] == "Error date not found!"

def test_date_invalid():    
    assert calc_exchange(10, "EUR", "USD", "2030-01-01")["message"] == "Error date not found!"
