"""UK city weather analysis for 2025 sample data."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent
df = pd.read_csv(HERE / "weather.csv", parse_dates=["date"])
df["month"] = df["date"].dt.month

def md_table(frame: pd.DataFrame) -> str:
    cols = list(frame.columns)
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in frame.iterrows():
        lines.append("| " + " | ".join(str(row[c]) for c in cols) + " |")
    return "\n".join(lines)

city = (
    df.groupby("city")
    .agg(avg_temp=("temp_c", "mean"), total_rain=("rainfall_mm", "sum"), avg_humidity=("humidity_pct", "mean"))
    .round(1)
    .reset_index()
    .sort_values("avg_temp", ascending=False)
)
monthly = df.groupby(["month", "city"], as_index=False)["temp_c"].mean()

fig, ax = plt.subplots(figsize=(10, 4.5))
for c, part in monthly.groupby("city"):
    ax.plot(part["month"], part["temp_c"], marker="o", label=c)
ax.set_xticks(range(1, 13))
ax.set_xlabel("Month")
ax.set_ylabel("Avg temp (°C)")
ax.set_title("Average temperature by city and month")
ax.legend()
fig.tight_layout()
fig.savefig(HERE / "weather_temps.png", dpi=140)
plt.close()

fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(city["city"], city["total_rain"], color="#0284c7")
ax.set_title("Total rainfall (mm)")
fig.tight_layout()
fig.savefig(HERE / "weather_rain.png", dpi=140)
plt.close()

wettest = df.loc[df["rainfall_mm"].idxmax()]
hottest = df.loc[df["temp_c"].idxmax()]

report = f"""# Weather analysis

Sample daily weather for London, Manchester, Birmingham, and Edinburgh in 2025 ({len(df)} rows).

## City summary

{md_table(city)}

## Highlights

- Warmest city on average: **{city.iloc[0]['city']}** ({city.iloc[0]['avg_temp']}°C)
- Hottest day: **{hottest['date'].date()}** in {hottest['city']} ({hottest['temp_c']}°C)
- Wettest day: **{wettest['date'].date()}** in {wettest['city']} ({wettest['rainfall_mm']} mm)

See `weather_temps.png` and `weather_rain.png`.
"""
(HERE / "REPORT.md").write_text(report)
print("weather done")
