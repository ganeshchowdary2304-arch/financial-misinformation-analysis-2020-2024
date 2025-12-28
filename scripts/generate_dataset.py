import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

num_events = 1100

cities = [
    ("London", 51.5074, -0.1278),
    ("Manchester", 53.4808, -2.2426),
    ("Birmingham", 52.4862, -1.8904),
    ("Leeds", 53.8008, -1.5491),
    ("Bristol", 51.4545, -2.5879)
]

narratives = [
    "Fake Insolvency Rumour",
    "Deepfake Executive Announcement",
    "Synthetic Regulatory Announcement",
    "AI-Generated Interest Rate Rumour",
    "False Cyberattack Alert",
    "Fraudulent Investment Scheme"
]

weights_city = [0.55, 0.15, 0.12, 0.10, 0.08]
weights_narr = [0.23, 0.21, 0.19, 0.15, 0.13, 0.09]

start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 12, 31)

def random_date(start, end):
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

data = []

for i in range(1, num_events + 1):
    city, lat, lon = random.choices(cities, weights=weights_city)[0]
    narrative = random.choices(narratives, weights=weights_narr)[0]
    date = random_date(start_date, end_date)

    tone = int(np.clip(np.random.normal(-6, 2.5), -10, 10))
    mentions = random.randint(5, 35)

    desc = f"This event involved a {narrative.lower()} reported in {city}."

    data.append([
        i,
        date.strftime("%Y-%m-%d"),
        date.year,
        date.month,
        city,
        lat,
        lon,
        narrative,
        tone,
        mentions,
        desc,
        "Financial Sector"
    ])

columns = [
    "event_id", "date", "year", "month", "city", "latitude", "longitude",
    "narrative_type", "tone_score", "mentions", "description", "sector_reference"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("data/financial_misinformation_2020_2024_full_dataset.csv", index=False)
print("Dataset generated successfully.")
