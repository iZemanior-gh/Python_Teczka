import requests

def pobierz_euro():
    url = "http://api.nbp.pl/api/exchangerates/rates/a/eur/?format=json"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    return data['rates'][0]['mid']