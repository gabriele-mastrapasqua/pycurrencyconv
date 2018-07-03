# Python currency converter

This is a simple flask REST API in python3 that convert the provided amount​ from src_currency​ to dest_currency​,
given the exchange rate at the reference_date​. 
The last 90 days exchange rates are scraped from this link: https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml

The api is callable like this:

```
curl -X POST -H "Content-Type: application/json" -d '{"amount": 12.35, "src_currency": "EUR", "dest_currency": "USD", "reference_date": "2018-07-02"}' http://localhost:5000/calc_exchange/
```

The response is a JSON object like:
```
{"amount": 14.374165, "currency": "USD"}
```

---

To build with docker:

## build

```
docker build . -t pyconv
```

## to run

```
docker run --name pyconv -p 5000:5000 -d pyconv
```


## to stop

```
docker stop pyconv
docker rm pyconv
```

## to test

```
docker exec -it pyconv pytest
```

