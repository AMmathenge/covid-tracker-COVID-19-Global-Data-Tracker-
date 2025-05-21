# visualizer.py
import matplotlib.pyplot as plt
import pandas as pd

def plot_cases_over_time(country):
    """Plot historical cases for a country using Johns Hopkins data."""
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    df = pd.read_csv(url)
    country_data = df[df['Country/Region'] == country].iloc[:, 4:].sum()
    dates = pd.to_datetime(country_data.index)
    cases = country_data.values

    plt.figure(figsize=(10, 6))
    plt.plot(dates, cases, marker='o', linestyle='-')
    plt.title(f"COVID-19 Cases Over Time in {country}")
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()