
from pathlib import Path
import sqlite3
import pandas as pd

# Find the project folder
PROJECT_DIR = Path(__file__).resolve().parent

# File paths
CSV_FILE = PROJECT_DIR / "data" / "travel_bookings_clean.csv"
DB_FILE = PROJECT_DIR / "data" / "travel_bookings.db"

# Load the cleaned dataset
df = pd.read_csv(CSV_FILE)

# Convert date columns to consistent date strings
for column in ["booking_date", "travel_date"]:
    df[column] = pd.to_datetime(df[column]).dt.strftime("%Y-%m-%d")

# Create the database and load the data
with sqlite3.connect(DB_FILE) as connection:
    df.to_sql("bookings", connection, if_exists="replace", index=False)

    # Verify that the records were loaded
    row_count = pd.read_sql_query(
        "SELECT COUNT(*) AS total_records FROM bookings",
        connection
    )

print("Database created successfully!")
print(f"Database location: {DB_FILE}")
print(f"Records loaded: {row_count.iloc[0]['total_records']}")
print("\nSample records:")
print(df.head().to_string(index=False))
