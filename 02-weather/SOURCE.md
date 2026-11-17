# Source: Australian weather

- **Dataset:** `weather_australia` (daily weather for Wollongong, Hobart, and Uluru; 300 rows, 100 per station; years 2008-2020)
- **Original data:** Australian Bureau of Meteorology daily observations, as packaged in the `weatherAUS` data of the R package `rattle`
- **Mirror used:** R package `bayesrules`, via the Rdatasets collection on GitHub: `bayesrules/weather_australia.csv`. The package describes it as a sub-sample of the `weatherAUS` data.
- **Retrieved by:** `fetch_data.py`, which keeps location, min/max temperature, rainfall, year, month, and day of year and writes `02-weather/weather_australia.csv`
- **Missing values:** a few rows have blanks; the analysis drops rows missing temperature or rainfall
- **Terms:** check the Bureau of Meteorology terms before reusing the data
