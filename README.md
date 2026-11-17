# Data analysis projects

Beginner projects for [aiakshayshet-web](https://github.com/aiakshayshet-web). Each folder has a public dataset (CSV), a Python script, charts, a short report, and a `SOURCE.md` with where the data came from.

## Projects

| Folder | Question | How to run |
| --- | --- | --- |
| `01-sales` | How did California avocado revenue, price, and volume change week to week and year to year? | `python 01-sales/analyze_sales.py` |
| `02-weather` | How do three Australian stations (Wollongong, Hobart, Uluru) compare on temperature and rain? | `python 02-weather/analyze_weather.py` |
| `03-student-scores` | How do reading and math scores change by grade and kindergarten class size? (Project STAR) | `python 03-student-scores/analyze_scores.py` |

## Setup

```bash
python -m pip install -r requirements.txt
python fetch_data.py   # optional: re-download the public data and rebuild the cleaned CSVs
python 01-sales/analyze_sales.py
python 02-weather/analyze_weather.py
python 03-student-scores/analyze_scores.py
```

Each analysis writes `REPORT.md` and PNG charts in its folder. The cleaned CSVs are committed, so the analyses run offline. `fetch_data.py` downloads the source files from GitHub (via the Rdatasets collection) and rebuilds them.

## Skills practiced

- Load CSV with pandas
- Group, aggregate, sort
- Charts with matplotlib
- Write a short findings report

Data is real public data, not generated or live API data. See each folder's `SOURCE.md` for the original source and retrieval details.
