"""Avocado sales analysis: revenue, price, and volume over time (California, 2015-2018).

Revenue is estimated as AveragePrice x TotalVolume for each week.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent
df = pd.read_csv(HERE / "avocado.csv", parse_dates=["date"])
df["revenue"] = df["AveragePrice"] * df["TotalVolume"]
df["month"] = df["date"].dt.to_period("M").astype(str)
df["year"] = df["date"].dt.year


def md_table(frame: pd.DataFrame) -> str:
    cols = list(frame.columns)
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for row in frame.itertuples(index=False):
        lines.append("| " + " | ".join(str(v) for v in row) + " |")
    return "\n".join(lines)


total_revenue = df["revenue"].sum()
total_volume = df["TotalVolume"].sum()
weeks = len(df)
avg_price = df["AveragePrice"].mean()

by_month = (
    df.groupby("month", as_index=False)
    .agg(revenue=("revenue", "sum"), volume=("TotalVolume", "sum"), avg_price=("AveragePrice", "mean"))
)
by_year = (
    df.groupby("year")
    .agg(weeks=("date", "count"), revenue=("revenue", "sum"), avg_price=("AveragePrice", "mean"), avg_weekly_volume=("TotalVolume", "mean"))
    .round({"revenue": 0, "avg_price": 2, "avg_weekly_volume": 0})
    .reset_index()
)
by_year["revenue"] = by_year["revenue"].map(lambda v: f"{v:,.0f}")
by_year["avg_weekly_volume"] = by_year["avg_weekly_volume"].map(lambda v: f"{v:,.0f}")

best = by_month.loc[by_month["revenue"].idxmax()]
peak_price = by_month.loc[by_month["avg_price"].idxmax()]

fig, ax = plt.subplots(figsize=(10, 4.5))
ax.plot(by_month["month"], by_month["revenue"] / 1e6, marker="o", color="#7c3aed")
ax.set_title("Estimated monthly avocado revenue, California (conventional)")
ax.set_ylabel("Revenue (millions)")
ax.tick_params(axis="x", rotation=60)
fig.tight_layout()
fig.savefig(HERE / "sales_trend.png", dpi=140)
plt.close()

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
axes[0].scatter(df["AveragePrice"], df["TotalVolume"] / 1e6, alpha=0.6, color="#2563eb")
axes[0].set_title("Weekly price vs volume")
axes[0].set_xlabel("Average price ($)")
axes[0].set_ylabel("Volume sold (millions)")
axes[1].bar(by_year["year"].astype(str), by_year["avg_price"], color="#059669")
axes[1].set_title("Average price by year")
axes[1].set_ylabel("Average price ($)")
fig.tight_layout()
fig.savefig(HERE / "sales_charts.png", dpi=140)
plt.close()

corr = df["AveragePrice"].corr(df["TotalVolume"])

report = f"""# Sales analysis: avocados in California

**Dataset:** `{weeks}` weekly observations, {df['date'].min().date()} to {df['date'].max().date()}, conventional avocados sold in California. Source: the `avocado` dataset (Hass Avocado Board data, via Kiggins 2018 and the R `causaldata` package). See `SOURCE.md`.

Revenue is estimated as weekly average price x total volume sold.

| Metric | Value |
| --- | ---: |
| Estimated total revenue | {total_revenue:,.0f} |
| Total avocados sold | {total_volume:,.0f} |
| Average weekly price | {avg_price:.2f} |

## By year

Note: 2018 is a partial year (data ends in March).

{md_table(by_year)}

## Findings

- Best month for revenue: **{best['month']}** ({best['revenue']:,.0f}). Months contain 4 or 5 weeks, so this is a total, not a weekly average.
- Highest average price month: **{peak_price['month']}** ({peak_price['avg_price']:.2f})
- Price and volume correlation across weeks: **{corr:.2f}**

See `sales_trend.png` and `sales_charts.png`.
"""
(HERE / "REPORT.md").write_text(report)
print("sales done")
