"""Student score analysis by subject and year group."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent
df = pd.read_csv(HERE / "scores.csv")

def md_table(frame: pd.DataFrame) -> str:
    cols = list(frame.columns)
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in frame.iterrows():
        lines.append("| " + " | ".join(str(row[c]) for c in cols) + " |")
    return "\n".join(lines)

by_subject = df.groupby("subject")["score"].agg(mean="mean", median="median", min="min", max="max").round(1).reset_index()
by_year = df.groupby("year")["score"].agg(mean="mean", students="nunique").round(1).reset_index()
pass_mark = 50
df["passed"] = df["score"] >= pass_mark
pass_rate = df["passed"].mean() * 100
top = df.groupby(["student_id", "name"], as_index=False)["score"].mean().sort_values("score", ascending=False).head(5).round(1)

fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(by_subject["subject"], by_subject["mean"], color="#dc2626")
ax.set_ylim(0, 100)
ax.set_title("Average score by subject")
ax.set_ylabel("Mean score")
fig.tight_layout()
fig.savefig(HERE / "scores_by_subject.png", dpi=140)
plt.close()

fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(df["score"], bins=15, color="#f59e0b", edgecolor="white")
ax.set_title("Score distribution")
ax.set_xlabel("Score")
ax.set_ylabel("Count")
fig.tight_layout()
fig.savefig(HERE / "scores_hist.png", dpi=140)
plt.close()

report = f"""# Student scores analysis

{df['student_id'].nunique()} students across years 10–12, four subjects, {len(df)} scores.

## By subject

{md_table(by_subject)}

## By year group

{md_table(by_year)}

## Highlights

- Pass rate (≥ {pass_mark}): **{pass_rate:.1f}%**
- Strongest subject (mean): **{by_subject.loc[by_subject['mean'].idxmax(), 'subject']}**
- Top 5 students by average:

{md_table(top)}

See `scores_by_subject.png` and `scores_hist.png`.
"""
(HERE / "REPORT.md").write_text(report)
print("scores done")
