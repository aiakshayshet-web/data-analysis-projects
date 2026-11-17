"""Download the public datasets used by the three projects and write cleaned CSVs.

Sources (all mirrored in the Rdatasets collection on GitHub):
  - causaldata/avocado          -> 01-sales/avocado.csv
  - bayesrules/weather_australia -> 02-weather/weather_australia.csv
  - AER/STAR                    -> 03-student-scores/star_scores.csv

Run `python fetch_data.py` to regenerate the CSVs. The cleaned files are
committed too, so the analyses run offline.
"""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).parent
BASE = "https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv"


def fetch_avocado() -> pd.DataFrame:
    df = pd.read_csv(f"{BASE}/causaldata/avocado.csv")
    out = df[["Date", "AveragePrice", "TotalVolume"]].rename(columns={"Date": "date"})
    out["date"] = pd.to_datetime(out["date"]).dt.strftime("%Y-%m-%d")
    return out.sort_values("date")


def fetch_weather() -> pd.DataFrame:
    df = pd.read_csv(f"{BASE}/bayesrules/weather_australia.csv")
    cols = ["location", "mintemp", "maxtemp", "rainfall", "year", "month", "day_of_year"]
    return df[cols].sort_values(["location", "year", "day_of_year"])


def fetch_star() -> pd.DataFrame:
    """Reshape Project STAR from one row per student to one row per student-grade."""
    df = pd.read_csv(f"{BASE}/AER/STAR.csv", low_memory=False)
    grades = {"k": "K", "1": "1", "2": "2", "3": "3"}
    frames = []
    for suffix, label in grades.items():
        part = pd.DataFrame({
            "student_id": df["rownames"],
            "class_type": df["stark"],
            "gender": df["gender"],
            "ethnicity": df["ethnicity"],
            "grade": label,
            "reading": df[f"read{suffix}"],
            "math": df[f"math{suffix}"],
        })
        frames.append(part.dropna(subset=["reading", "math"], how="all"))
    out = pd.concat(frames, ignore_index=True)
    return out.sort_values(["student_id", "grade"]).reset_index(drop=True)


def main() -> None:
    jobs = {
        ROOT / "01-sales" / "avocado.csv": fetch_avocado,
        ROOT / "02-weather" / "weather_australia.csv": fetch_weather,
        ROOT / "03-student-scores" / "star_scores.csv": fetch_star,
    }
    for path, fn in jobs.items():
        df = fn()
        df.to_csv(path, index=False)
        print(f"wrote {path.relative_to(ROOT)} ({len(df)} rows)")


if __name__ == "__main__":
    main()
