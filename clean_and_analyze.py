
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# 1. SET UP PROJECT PATHS
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"
IMAGES_DIR = PROJECT_DIR / "images"

IMAGES_DIR.mkdir(exist_ok=True)

RAW_FILE = DATA_DIR / "travel_bookings.csv"
CLEAN_FILE = DATA_DIR / "travel_bookings_clean.csv"

# --------------------------------------------------
# 2. LOAD THE RAW DATA
# --------------------------------------------------

df = pd.read_csv(RAW_FILE)

print("=" * 55)
print("RAW DATA")
print("=" * 55)
print(f"Original rows: {len(df)}")

# Keep the original file unchanged.
# All cleaning is performed on the DataFrame in memory.

# --------------------------------------------------
# 3. STANDARDIZE COLUMN NAMES AND TEXT
# --------------------------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

text_columns = [
    "destination",
    "travel_class",
    "booking_channel",
    "booking_status"
]

for column in text_columns:
    df[column] = df[column].str.strip()

# Standardize capitalization consistently.
df["destination"] = df["destination"].str.title()
df["travel_class"] = df["travel_class"].str.title()
df["booking_channel"] = df["booking_channel"].str.title()
df["booking_status"] = df["booking_status"].str.title()

# --------------------------------------------------
# 4. CONVERT DATA TYPES
# --------------------------------------------------

df["booking_id"] = pd.to_numeric(
    df["booking_id"], errors="coerce"
)

df["customer_id"] = pd.to_numeric(
    df["customer_id"], errors="coerce"
)

df["booking_price"] = pd.to_numeric(
    df["booking_price"], errors="coerce"
)

df["booking_date"] = pd.to_datetime(
    df["booking_date"], errors="coerce"
)

df["travel_date"] = pd.to_datetime(
    df["travel_date"], errors="coerce"
)

# --------------------------------------------------
# 5. CHECK DATA QUALITY
# --------------------------------------------------

print("\n" + "=" * 55)
print("DATA QUALITY CHECKS")
print("=" * 55)

print("\nMissing values before cleaning:")
print(df.isnull().sum())

print("\nExact duplicate rows:", df.duplicated().sum())
print(
    "Duplicate booking IDs:",
    df["booking_id"].duplicated().sum()
)

# Remove exact duplicate records only.
df = df.drop_duplicates()

# Remove records missing essential identifiers or dates.
essential_columns = [
    "booking_id",
    "customer_id",
    "booking_date",
    "travel_date"
]

rows_before = len(df)
df = df.dropna(subset=essential_columns)
print("Rows removed for missing essential fields:", rows_before - len(df))

# Remove records with invalid numeric values.
rows_before = len(df)
df = df[
    (df["booking_id"] > 0)
    & (df["customer_id"] > 0)
    & (df["booking_price"] > 0)
].copy()
print("Rows removed for invalid IDs or prices:", rows_before - len(df))

# Validate booking IDs are unique.
# We do not arbitrarily keep one row if an ID is duplicated.
if df["booking_id"].duplicated().any():
    raise ValueError(
        "Duplicate booking IDs remain. Investigate before continuing."
    )

# Validate dates.
invalid_dates = df["travel_date"] < df["booking_date"]
print("Records with travel before booking:", invalid_dates.sum())

if invalid_dates.any():
    raise ValueError(
        "Invalid travel dates found. Investigate before continuing."
    )

# Validate allowed categories.
allowed_statuses = {"Confirmed", "Cancelled", "Completed"}
allowed_classes = {"Economy", "Premium Economy", "Business"}
allowed_channels = {"Website", "Mobile App", "Travel Agent"}

if not set(df["booking_status"].dropna()).issubset(allowed_statuses):
    raise ValueError("Unexpected booking status found.")

if not set(df["travel_class"].dropna()).issubset(allowed_classes):
    raise ValueError("Unexpected travel class found.")

if not set(df["booking_channel"].dropna()).issubset(allowed_channels):
    raise ValueError("Unexpected booking channel found.")

if df[text_columns].isnull().any().any():
    raise ValueError(
        "Missing categorical values found. Investigate before continuing."
    )

# --------------------------------------------------
# 6. CREATE ANALYSIS COLUMNS
# --------------------------------------------------

df["booking_month"] = df["booking_date"].dt.to_period("M").astype(str)

# This is the recorded booking price, not verified company revenue.
df["booking_price"] = df["booking_price"].round(2)

# --------------------------------------------------
# 7. SAVE THE CLEANED DATA
# --------------------------------------------------

df.to_csv(CLEAN_FILE, index=False)

print("\n" + "=" * 55)
print("CLEANING RESULTS")
print("=" * 55)
print(f"Cleaned rows: {len(df)}")
print(f"Cleaned columns: {len(df.columns)}")
print(f"Cleaned file saved to: {CLEAN_FILE}")
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# --------------------------------------------------
# 8. EXPLORE BOOKING STATUS
# --------------------------------------------------

sns.set_theme(style="whitegrid")

status_counts = df["booking_status"].value_counts()

print("\nBooking status counts:")
print(status_counts)

plt.figure(figsize=(8, 5))
sns.countplot(
    data=df,
    x="booking_status",
    order=status_counts.index
)
plt.title("Bookings by Status")
plt.xlabel("Booking Status")
plt.ylabel("Number of Bookings")
plt.tight_layout()
plt.savefig(IMAGES_DIR / "booking_status.png", dpi=150)
plt.close()

# --------------------------------------------------
# 9. EXPLORE POPULAR DESTINATIONS
# --------------------------------------------------

destination_counts = (
    df["destination"]
    .value_counts()
    .sort_values(ascending=False)
)

print("\nBookings by destination:")
print(destination_counts)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=destination_counts.values,
    y=destination_counts.index
)
plt.title("Bookings by Destination")
plt.xlabel("Number of Bookings")
plt.ylabel("Destination")
plt.tight_layout()
plt.savefig(IMAGES_DIR / "bookings_by_destination.png", dpi=150)
plt.close()

# --------------------------------------------------
# 10. EXPLORE BOOKING CHANNELS
# --------------------------------------------------

channel_counts = df["booking_channel"].value_counts()

print("\nBookings by channel:")
print(channel_counts)

plt.figure(figsize=(8, 5))
sns.barplot(
    x=channel_counts.values,
    y=channel_counts.index
)
plt.title("Bookings by Channel")
plt.xlabel("Number of Bookings")
plt.ylabel("Booking Channel")
plt.tight_layout()
plt.savefig(IMAGES_DIR / "booking_channels.png", dpi=150)
plt.close()

# --------------------------------------------------
# 11. EXPLORE MONTHLY BOOKING TRENDS
# --------------------------------------------------

monthly_bookings = (
    df.groupby("booking_month")
    .size()
    .rename("booking_count")
    .reset_index()
)

print("\nMonthly booking counts:")
print(monthly_bookings.to_string(index=False))

plt.figure(figsize=(13, 5))
sns.lineplot(
    data=monthly_bookings,
    x="booking_month",
    y="booking_count",
    marker="o"
)
plt.title("Monthly Booking Volume")
plt.xlabel("Booking Month")
plt.ylabel("Number of Bookings")
plt.xticks(rotation=60)
plt.tight_layout()
plt.savefig(IMAGES_DIR / "monthly_bookings.png", dpi=150)
plt.close()

# --------------------------------------------------
# 12. EXPLORE PRICE DISTRIBUTION
# --------------------------------------------------

print("\nBooking price summary:")
print(df["booking_price"].describe().round(2))

plt.figure(figsize=(9, 5))
sns.histplot(df["booking_price"], bins=30, kde=True)
plt.title("Distribution of Booking Prices")
plt.xlabel("Booking Price (synthetic price units)")
plt.ylabel("Number of Bookings")
plt.tight_layout()
plt.savefig(IMAGES_DIR / "price_distribution.png", dpi=150)
plt.close()

# --------------------------------------------------
# 13. FINAL SUMMARY
# --------------------------------------------------

print("\n" + "=" * 55)
print("ANALYSIS COMPLETE")
print("=" * 55)
print(f"Rows analyzed: {len(df)}")
print(f"Unique customers: {df['customer_id'].nunique()}")
print(f"Destinations: {df['destination'].nunique()}")
print(f"Charts saved in: {IMAGES_DIR}")
