"""Create the sample CSV files used by the three analysis projects."""

import csv
import os
import random
from datetime import datetime, timedelta

random.seed(42)
ROOT = os.path.dirname(os.path.abspath(__file__))
start = datetime(2025, 1, 1)

products = ["Laptop", "Phone", "Headphones", "Keyboard", "Monitor", "Mouse"]
regions = ["North", "South", "East", "West"]
prices = {"Laptop": 850, "Phone": 620, "Headphones": 80, "Keyboard": 45, "Monitor": 220, "Mouse": 25}
rows = []
for _ in range(400):
    d = start + timedelta(days=random.randint(0, 364))
    product = random.choice(products)
    region = random.choice(regions)
    qty = random.randint(1, 8)
    price = round(prices[product] * random.uniform(0.85, 1.15), 2)
    rows.append([d.strftime("%Y-%m-%d"), product, region, qty, price, round(qty * price, 2)])
rows.sort()
os.makedirs(os.path.join(ROOT, "01-sales"), exist_ok=True)
with open(os.path.join(ROOT, "01-sales", "sales.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["date", "product", "region", "quantity", "unit_price", "revenue"])
    w.writerows(rows)

cities = ["London", "Manchester", "Birmingham", "Edinburgh"]
temps = {1: 6, 2: 6, 3: 8, 4: 11, 5: 14, 6: 17, 7: 19, 8: 18, 9: 16, 10: 12, 11: 8, 12: 6}
wrows = []
for i in range(365):
    d = start + timedelta(days=i)
    for city in cities:
        temp = round(temps[d.month] + random.uniform(-4, 4) + (1.5 if city == "London" else 0), 1)
        rain = max(0, round(random.gauss(2.0 if d.month in (10, 11, 12, 1) else 1.2, 2.2), 1))
        humidity = min(99, max(40, int(random.gauss(75, 10))))
        wrows.append([d.strftime("%Y-%m-%d"), city, temp, rain, humidity])
os.makedirs(os.path.join(ROOT, "02-weather"), exist_ok=True)
with open(os.path.join(ROOT, "02-weather", "weather.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["date", "city", "temp_c", "rainfall_mm", "humidity_pct"])
    w.writerows(wrows)

subjects = ["Maths", "English", "Science", "History"]
srows = []
for sid in range(1, 81):
    name = f"Student{sid:02d}"
    year = random.choice([10, 11, 12])
    for subj in subjects:
        score = int(min(100, max(35, random.gauss(68 + (2 if year == 12 else 0), 12))))
        srows.append([sid, name, year, subj, score])
os.makedirs(os.path.join(ROOT, "03-student-scores"), exist_ok=True)
with open(os.path.join(ROOT, "03-student-scores", "scores.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["student_id", "name", "year", "subject", "score"])
    w.writerows(srows)

print("Wrote sales.csv, weather.csv, and scores.csv")
