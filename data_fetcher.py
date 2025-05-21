# data_fetcher.py
import requests

def fetch_global_data():
    """Fetch global COVID-19 stats."""
    url = "https://disease.sh/v3/covid-19/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch global data.")
        return None

def fetch_country_data(country):
    """Fetch data for a specific country."""
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {country}.")
        return None