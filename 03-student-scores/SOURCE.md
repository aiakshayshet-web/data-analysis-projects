# Source: Project STAR

- **Dataset:** Project STAR (Student-Teacher Achievement Ratio), a Tennessee experiment in 1985-1989 that randomly assigned kindergarten students to small classes, regular classes, or regular classes with an aide
- **Mirror used:** R package `AER` (`STAR` data), via the Rdatasets collection on GitHub: `AER/STAR.csv`. It has 11,598 students, with reading and math scaled scores for kindergarten through grade 3.
- **Retrieved by:** `fetch_data.py`, which reshapes the file to one row per student and grade, keeps reading and math scores, and writes `03-student-scores/star_scores.csv`
- **Privacy:** the public-access file uses anonymous IDs; no names are included
- **Terms:** check the original Project STAR documentation before reuse
