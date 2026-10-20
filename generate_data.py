
import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

# Make the results reproducible
random.seed(42)

# Project folders
PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# Synthetic data options
destinations = [
    "London", "Paris", "Dubai", "Tokyo",
    "New York", "Singapore", "Sydney", "Rome"
]

booking_statuses = [
    "Confirmed", "Confirmed", "Confirmed",
    "Cancelled", "Completed"
]

travel_classes = ["Economy", "Premium Economy", "Business"]
booking_channels = ["Website", "Mobile App", "Travel Agent"]

start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 12, 31)
date_range_days = (end_date - start_date).days

records = []

# Generate 1,000 fictional bookings
for booking_id in range(1, 1001):
    booking_date = start_date + timedelta(
        days=random.randint(0, date_range_days)
    )

    travel_date = booking_date + timedelta(
        days=random.randint(7, 180)
    )

    destination = random.choice(destinations)
    status = random.choice(booking_statuses)
    travel_class = random.choice(travel_classes)
    channel = random.choice(booking_channels)

    # Synthetic price based on travel class
    base_price = {
        "Economy": 250,
        "Premium Economy": 600,
        "Business": 1500
    }[travel_class]

    price = round(base_price * random.uniform(0.7, 1.8), 2)

    records.append({
        "booking_id": booking_id,
        "customer_id": random.randint(1001, 1300),
        "booking_date": booking_date.date(),
        "travel_date": travel_date.date(),
        "destination": destination,
        "travel_class": travel_class,
        "booking_channel": channel,
        "booking_status": status,
        "booking_price": price
    })

# Create a DataFrame and save it as CSV
df = pd.DataFrame(records)

output_file = DATA_DIR / "travel_bookings.csv"
df.to_csv(output_file, index=False)

print("Dataset created successfully!")
print(f"File location: {output_file}")
print(f"Number of bookings: {len(df)}")
print("\nFirst five records:")
print(df.head())
