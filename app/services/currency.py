import requests

EXCHANGE_API_URL = "https://open.er-api.com/v6/latest"

def get_exchange_rates(base_currency: str):
    url = f"{EXCHANGE_API_URL}/{base_currency}"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        raise Exception("Failed to fetch exchange rates")

    data = response.json()

    if data.get("result") != "success":
        raise Exception("Exchange API returned error")

    return data.get("rates", {})