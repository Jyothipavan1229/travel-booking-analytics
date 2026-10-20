
from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "data" / "travel_bookings_clean.csv"
REPORT_DIR = PROJECT_DIR / "reports"

REPORT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_FILE)
df["booking_date"] = pd.to_datetime(df["booking_date"])

# 1. Overall dataset summary
total_bookings = len(df)
unique_customers = df["customer_id"].nunique()
unique_destinations = df["destination"].nunique()

print("=" * 55)
print("OVERALL SUMMARY")
print("=" * 55)
print(f"Total booking records: {total_bookings}")
print(f"Unique customers: {unique_customers}")
print(f"Unique destinations: {unique_destinations}")

# 2. Booking status
status_summary = (
    df["booking_status"]
    .value_counts()
    .rename_axis("booking_status")
    .reset_index(name="bookings")
)

status_summary["percentage"] = (
    status_summary["bookings"] / total_bookings * 100
).round(2)

print("\nBOOKING STATUS")
print(status_summary.to_string(index=False))

# 3. Destination ranking
destination_summary = (
    df.groupby("destination")
    .size()
    .sort_values(ascending=False)
    .rename("bookings")
    .reset_index()
)

destination_summary["percentage"] = (
    destination_summary["bookings"] / total_bookings * 100
).round(2)

print("\nDESTINATION RANKING")
print(destination_summary.to_string(index=False))

# 4. Booking channels
channel_summary = (
    df.groupby("booking_channel")
    .size()
    .sort_values(ascending=False)
    .rename("bookings")
    .reset_index()
)

channel_summary["percentage"] = (
    channel_summary["bookings"] / total_bookings * 100
).round(2)

print("\nBOOKING CHANNELS")
print(channel_summary.to_string(index=False))

# 5. Price summary
print("\nBOOKING PRICE SUMMARY")
print(df["booking_price"].describe().round(2).to_string())

# 6. Monthly booking volume
monthly = (
    df.assign(month=df["booking_date"].dt.to_period("M").astype(str))
    .groupby("month")
    .size()
)

print("\nMONTHLY BOOKING VOLUME")
print(monthly.to_string())

print("\nHighest-volume month:", monthly.idxmax())
print("Bookings in that month:", int(monthly.max()))
print("Lowest-volume month:", monthly.idxmin())
print("Bookings in that month:", int(monthly.min()))

# 7. Save summary tables for later reporting
status_summary.to_csv(
    REPORT_DIR / "booking_status_summary.csv", index=False
)
destination_summary.to_csv(
    REPORT_DIR / "destination_summary.csv", index=False
)
channel_summary.to_csv(
    REPORT_DIR / "channel_summary.csv", index=False
)

print("\nSummary tables saved in:", REPORT_DIR)
