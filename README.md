# Data analysis projects

Beginner projects for [aiakshayshet-web](https://github.com/aiakshayshet-web). Each folder has a CSV, a Python script, charts, and a short report.

## Projects

| Folder | Question | How to run |
| --- | --- | --- |
| `01-sales` | Which products and regions make the most revenue? | `python 01-sales/analyze_sales.py` |
| `02-weather` | How do UK cities compare on temperature and rain? | `python 02-weather/analyze_weather.py` |
| `03-student-scores` | How do scores differ by subject and year? | `python 03-student-scores/analyze_scores.py` |

## Setup

```bash
python -m pip install pandas matplotlib
python generate_data.py
python 01-sales/analyze_sales.py
python 02-weather/analyze_weather.py
python 03-student-scores/analyze_scores.py
```

Each analysis writes `REPORT.md` and PNG charts in its folder. `generate_data.py` recreates the CSVs with a fixed random seed.

## Skills practiced

- Load CSV with pandas
- Group, aggregate, sort
- Charts with matplotlib
- Write a short findings report

Data is generated sample data (not live APIs), so the repo runs offline.
