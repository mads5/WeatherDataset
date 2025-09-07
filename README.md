# WeatherDataset

This project provides a small utility script to collect the current date and weather information for a given city using [wttr.in](https://wttr.in) and store the results in an Excel file.

## Usage

```
python collect_weather.py <city>
```

Running the script appends a row with the current date, city name, and weather summary to `weather_data.xlsx` in the repository root.

## Requirements

- Python 3
- `requests`
- `pandas`
- `openpyxl`

Install dependencies with:

```
pip install requests pandas openpyxl
```
