# Source: avocado sales

- **Dataset:** `avocado` (weekly average price and total volume of conventional avocados sold in California, 169 weeks, 2015-01-04 to 2018-03-25)
- **Original data:** Hass Avocado Board weekly sales, published on Kaggle by Justin Kiggins (2018), "avocado-prices"
- **Mirror used:** R package `causaldata`, via the Rdatasets collection on GitHub: `causaldata/avocado.csv`
- **Retrieved by:** `fetch_data.py`, which keeps `Date`, `AveragePrice`, and `TotalVolume` and writes `01-sales/avocado.csv`
- **Terms:** check the Kaggle listing before reusing the data
