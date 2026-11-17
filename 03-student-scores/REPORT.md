# Student scores analysis: Project STAR

6149 students in the class-size experiment, with reading and math scores in kindergarten through grade 3 (16864 student-grade records). Source: Project STAR public-access data (Tennessee, 1985-1989), via the R `AER` package. See `SOURCE.md`.

Scores are scaled test scores. Students with no recorded class type are excluded.

## By grade

| grade | students | reading_mean | math_mean |
| --- | --- | --- | --- |
| K | 5874 | 436.7 | 485.4 |
| 1 | 4437 | 526.8 | 534.5 |
| 2 | 3477 | 592.7 | 588.3 |
| 3 | 3076 | 624.2 | 626.4 |

## Mean math score by class type and grade

| class_type | math_K | math_1 | math_2 | math_3 |
| --- | --- | --- | --- | --- |
| small | 490.9 | 541.2 | 592.3 | 629.8 |
| regular | 483.2 | 531.7 | 587.5 | 624.7 |
| regular+aide | 482.8 | 531.2 | 585.3 | 625.0 |

## Highlights

- Kindergarten math, small classes minus regular classes: **+7.7** points (raw difference of means; no significance test)
- Strongest grade for reading: **3** (624.2)
- Strongest grade for math: **3** (626.4)

See `scores_by_class.png` and `scores_hist.png`.
