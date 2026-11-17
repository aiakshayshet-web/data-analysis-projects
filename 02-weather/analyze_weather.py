"""Weather comparison for three Australian stations (Wollongong, Hobart, Uluru).

The source is a sub-sample of 100 days per station across 2008-2020, so monthly
averages rest on a small number of days each.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent
df = pd.read_csv(HERE / "weather_australia.csv")
df = df.dropna(subset=["mintemp", "maxtemp", "rainfall"])


def md_table(frame: pd.DataFrame) -> str:
    cols = list(frame.columns)
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for row in frame.itertuples(index=False):
        lines.append("| " + " | ".join(str(v) for v in row) + " |")
    return "\n".join(lines)


df["rainy"] = df["rainfall"] > 0
city = (
    df.groupby("location")
    .agg(
        days=("maxtemp", "count"),
        avg_max_c=("maxtemp", "mean"),
        avg_min_c=("mintemp", "mean"),
        mean_rain_mm=("rainfall", "mean"),
        rainy_day_pct=("rainy", "mean"),
    )
    .round({"avg_max_c": 1, "avg_min_c": 1, "mean_rain_mm": 2})
    .reset_index()
)
city["rainy_day_pct"] = (city["rainy_day_pct"] * 100).round(1)
city = city.sort_values("avg_max_c", ascending=False)

monthly = df.groupby(["month", "location"], as_index=False)["maxtemp"].mean()

fig, ax = plt.subplots(figsize=(10, 4.5))
for loc, part in monthly.groupby("location"):
    ax.plot(part["month"], part["maxtemp"], marker="o", label=loc)
ax.set_xticks(range(1, 13))
ax.set_xlabel("Month")
ax.set_ylabel("Avg max temp (°C)")
ax.set_title("Average daily max temperature by station and month (sampled days)")
ax.legend()
fig.tight_layout()
fig.savefig(HERE / "weather_temps.png", dpi=140)
plt.close()

fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(city["location"], city["mean_rain_mm"], color="#0284c7")
ax.set_title("Mean daily rainfall (mm) in sampled days")
ax.set_ylabel("mm per day")
fig.tight_layout()
fig.savefig(HERE / "weather_rain.png", dpi=140)
plt.close()

wettest = df.loc[df["rainfall"].idxmax()]
hottest = df.loc[df["maxtemp"].idxmax()]

report = f"""# Weather analysis: three Australian stations

Daily weather for Wollongong, Hobart, and Uluru: {len(df)} usable days ({df['year'].min()}-{df['year'].max()}). Source: `weather_australia` (a sub-sample of the BoM data in the R `rattle` package, via the R `bayesrules` package). See `SOURCE.md`.

Only about 100 days per station are included, so treat monthly patterns as indicative.

## Station summary

{md_table(city)}

Rainy day = any recorded rainfall above 0 mm.

## Highlights

- Warmest station on average (max temp): **{city.iloc[0]['location']}** ({city.iloc[0]['avg_max_c']}°C)
- Hottest sampled day: **{hottest['location']}**, {hottest['maxtemp']}°C (year {hottest['year']}, month {hottest['month']})
- Wettest sampled day: **{wettest['location']}**, {wettest['rainfall']} mm (year {wettest['year']}, month {wettest['month']})

See `weather_temps.png` and `weather_rain.png`.
"""
(HERE / "REPORT.md").write_text(report)
print("weather done")
