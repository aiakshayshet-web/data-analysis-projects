"""Project STAR analysis: reading and math scores by grade and class type.

Project STAR randomly assigned students to small classes, regular classes, or
regular classes with a teacher's aide in kindergarten. Scores are scaled test
scores (not percentages).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent
df = pd.read_csv(HERE / "star_scores.csv")
GRADE_ORDER = ["K", "1", "2", "3"]
CLASS_ORDER = ["small", "regular", "regular+aide"]

# Only students with a recorded kindergarten class type are in the experiment.
assigned = df.dropna(subset=["class_type"]).copy()
assigned["grade"] = pd.Categorical(assigned["grade"], GRADE_ORDER, ordered=True)


def md_table(frame: pd.DataFrame) -> str:
    cols = list(frame.columns)
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for row in frame.itertuples(index=False):
        lines.append("| " + " | ".join(str(v) for v in row) + " |")
    return "\n".join(lines)


students = assigned["student_id"].nunique()
by_grade = (
    assigned.groupby("grade", observed=True)
    .agg(students=("student_id", "nunique"), reading_mean=("reading", "mean"), math_mean=("math", "mean"))
    .round(1)
    .reset_index()
)
by_class = (
    assigned.groupby(["class_type", "grade"], observed=True)[["reading", "math"]]
    .mean()
    .round(1)
    .reset_index()
)
by_class_wide = by_class.pivot(index="class_type", columns="grade", values="math").reindex(CLASS_ORDER)
by_class_wide.columns = [f"math_{c}" for c in by_class_wide.columns]
by_class_wide = by_class_wide.round(1).reset_index()

k3 = assigned[assigned["grade"] == "K"].groupby("class_type")["math"].mean().reindex(CLASS_ORDER)

fig, ax = plt.subplots(figsize=(9, 4.5))
width = 0.25
x = range(len(GRADE_ORDER))
for i, ctype in enumerate(CLASS_ORDER):
    part = by_class[by_class["class_type"] == ctype].set_index("grade").reindex(GRADE_ORDER)
    ax.bar([xi + (i - 1) * width for xi in x], part["math"], width, label=ctype)
ax.set_xticks(list(x))
ax.set_xticklabels(GRADE_ORDER)
ax.set_xlabel("Grade")
ax.set_ylabel("Mean math scaled score")
ax.set_title("Math scores by grade and kindergarten class type")
ax.set_ylim(400, 650)
ax.legend()
fig.tight_layout()
fig.savefig(HERE / "scores_by_class.png", dpi=140)
plt.close()

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.hist(assigned["reading"].dropna(), bins=30, alpha=0.6, label="Reading", color="#dc2626")
ax.hist(assigned["math"].dropna(), bins=30, alpha=0.6, label="Math", color="#2563eb")
ax.set_title("Score distribution (all grades)")
ax.set_xlabel("Scaled score")
ax.set_ylabel("Count")
ax.legend()
fig.tight_layout()
fig.savefig(HERE / "scores_hist.png", dpi=140)
plt.close()

gap = k3["small"] - k3["regular"]
report = f"""# Student scores analysis: Project STAR

{students} students in the class-size experiment, with reading and math scores in kindergarten through grade 3 ({len(assigned)} student-grade records). Source: Project STAR public-access data (Tennessee, 1985-1989), via the R `AER` package. See `SOURCE.md`.

Scores are scaled test scores. Students with no recorded class type are excluded.

## By grade

{md_table(by_grade)}

## Mean math score by class type and grade

{md_table(by_class_wide)}

## Highlights

- Kindergarten math, small classes minus regular classes: **{gap:+.1f}** points (raw difference of means; no significance test)
- Strongest grade for reading: **{by_grade.loc[by_grade['reading_mean'].idxmax(), 'grade']}** ({by_grade['reading_mean'].max()})
- Strongest grade for math: **{by_grade.loc[by_grade['math_mean'].idxmax(), 'grade']}** ({by_grade['math_mean'].max()})

See `scores_by_class.png` and `scores_hist.png`.
"""
(HERE / "REPORT.md").write_text(report)
print("scores done")
