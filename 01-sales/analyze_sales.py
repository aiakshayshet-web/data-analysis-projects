"""Sales analysis: totals by product, region, and month."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent
df = pd.read_csv(HERE / "sales.csv", parse_dates=["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)

def md_table(frame: pd.DataFrame) -> str:
    cols = list(frame.columns)
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in frame.iterrows():
        lines.append("| " + " | ".join(str(row[c]) for c in cols) + " |")
    return "\n".join(lines)

total_revenue = df["revenue"].sum()
total_orders = len(df)
avg_order = df["revenue"].mean()
by_product = df.groupby("product", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
by_region = df.groupby("region", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
by_month = df.groupby("month", as_index=False)["revenue"].sum()

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
axes[0].bar(by_product["product"], by_product["revenue"], color="#2563eb")
axes[0].set_title("Revenue by product")
axes[0].tick_params(axis="x", rotation=30)
axes[0].set_ylabel("Revenue")
axes[1].bar(by_region["region"], by_region["revenue"], color="#059669")
axes[1].set_title("Revenue by region")
fig.tight_layout()
fig.savefig(HERE / "sales_charts.png", dpi=140)
plt.close()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(by_month["month"], by_month["revenue"], marker="o", color="#7c3aed")
ax.set_title("Monthly revenue")
ax.tick_params(axis="x", rotation=45)
ax.set_ylabel("Revenue")
fig.tight_layout()
fig.savefig(HERE / "sales_trend.png", dpi=140)
plt.close()

report = f"""# Sales analysis

**Dataset:** `{len(df)}` orders in 2025.

| Metric | Value |
| --- | ---: |
| Total revenue | {total_revenue:,.2f} |
| Orders | {total_orders} |
| Average order value | {avg_order:,.2f} |

## Revenue by product

{md_table(by_product.round(2))}

## Revenue by region

{md_table(by_region.round(2))}

## Findings

- Top product: **{by_product.iloc[0]['product']}** ({by_product.iloc[0]['revenue']:,.2f})
- Top region: **{by_region.iloc[0]['region']}** ({by_region.iloc[0]['revenue']:,.2f})
- Best month: **{by_month.loc[by_month['revenue'].idxmax(), 'month']}**

See `sales_charts.png` and `sales_trend.png`.
"""
(HERE / "REPORT.md").write_text(report)
print("sales done")
