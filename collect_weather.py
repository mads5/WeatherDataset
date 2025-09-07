import sys
from datetime import datetime
from pathlib import Path

import pandas as pd
import requests


def get_weather(city: str) -> str:
    """Fetch weather information string from wttr.in for the given city."""
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    response.raise_for_status()
    return response.text.strip()


def main() -> None:
    if len(sys.argv) > 1:
        city = sys.argv[1]
    else:
        city = input("Enter city name: ").strip()
    weather_info = get_weather(city)
    date_str = datetime.now().date().isoformat()

    file_path = Path("weather_data.xlsx")
    if file_path.exists():
        df = pd.read_excel(file_path)
    else:
        df = pd.DataFrame(columns=["Date", "City", "Weather"])

    new_row = pd.DataFrame([{ "Date": date_str, "City": city, "Weather": weather_info }])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_excel(file_path, index=False)
    print(f"Saved weather data for {city} on {date_str} to {file_path}")


if __name__ == "__main__":
    main()
