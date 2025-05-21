# covid_tracker.py (updated)
import argparse
from data_fetcher import fetch_global_data, fetch_country_data
from visualizer import plot_cases_over_time

def display_global_stats():
    data = fetch_global_data()
    if data:
        print("\nGlobal COVID-19 Stats:")
        print(f"Cases: {data['cases']:,}")
        print(f"Deaths: {data['deaths']:,}")
        print(f"Recovered: {data['recovered']:,}")

def display_country_stats(country):
    data = fetch_country_data(country)
    if data:
        print(f"\nStats for {data['country']}:")
        print(f"Cases: {data['cases']:,}")
        print(f"Deaths: {data['deaths']:,}")
        print(f"Active: {data['active']:,}")
        print(f"Recovered: {data['recovered']:,}")

def main():
    parser = argparse.ArgumentParser(description="COVID-19 Data Tracker")
    parser.add_argument("--world", action="store_true", help="Show global stats")  # Changed from --global
    parser.add_argument("--country", type=str, help="Specify a country")
    parser.add_argument("--plot", type=str, help="Plot cases over time for a country")
    args = parser.parse_args()

    if args.world:  # Updated here
        display_global_stats()
    elif args.country:
        display_country_stats(args.country)
    elif args.plot:
        plot_cases_over_time(args.plot)
    else:
        print("Use flags: --world, --country <name>, or --plot <country>")  # Updated help message

if __name__ == "__main__":
    main()