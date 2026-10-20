
from pathlib import Path

import pandas as pd

# Locate the CSV file relative to this script
PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "data" / "travel_bookings.csv"

# Load the dataset
df = pd.read_csv(DATA_FILE)

print("=" * 50)
print("1. DATASET SIZE")
print("=" * 50)
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n" + "=" * 50)
print("2. COLUMN NAMES")
print("=" * 50)
print(df.columns.tolist())

print("\n" + "=" * 50)
print("3. FIRST FIVE ROWS")
print("=" * 50)
print(df.head())

print("\n" + "=" * 50)
print("4. DATA TYPES")
print("=" * 50)
print(df.dtypes)

print("\n" + "=" * 50)
print("5. MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())

print("\n" + "=" * 50)
print("6. DUPLICATE RECORDS")
print("=" * 50)
print(f"Duplicate rows: {df.duplicated().sum()}")
print(f"Duplicate booking IDs: {df['booking_id'].duplicated().sum()}")

print("\n" + "=" * 50)
print("7. NUMERIC SUMMARY")
print("=" * 50)
print(df[["customer_id", "booking_price"]].describe())

print("\n" + "=" * 50)
print("8. VALIDATION CHECKS")
print("=" * 50)

print("Missing booking IDs:", df["booking_id"].isnull().sum())
print("Invalid prices:", (df["booking_price"] <= 0).sum())
print(
    "Travel before booking:",
    (pd.to_datetime(df["travel_date"]) <
     pd.to_datetime(df["booking_date"])).sum()
)

allowed_statuses = {"Confirmed", "Cancelled", "Completed"}
unexpected_statuses = set(df["booking_status"].dropna()) - allowed_statuses
print("Unexpected booking statuses:", unexpected_statuses)

print("\nInspection complete.")
