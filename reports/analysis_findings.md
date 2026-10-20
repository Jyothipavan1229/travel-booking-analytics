
# Travel Booking & Customer Journey Analytics

## 1. Project Overview

This project explores a synthetic travel-booking dataset using
Python and pandas. The analysis covers data quality, booking
status, destination distribution, booking channels, monthly
booking volume, and booking-price distribution.

## 2. Dataset Description

- Records analyzed: [insert total]
- Unique customers: [insert total]
- Destinations represented: [insert total]
- Data period: January 2024–December 2025 booking dates
- Source: Synthetic data generated for this portfolio project

## 3. Data Quality and Preparation

The analysis included checks for missing values, duplicate
records, duplicate booking IDs, invalid prices, date consistency,
and unexpected category values.

Date fields were converted to datetime types, categorical text
was standardized, and the cleaned dataset was saved separately
from the original data.

## 4. Findings

### Booking Status

[Insert the counts and percentages from the status summary.
Describe the distribution without claiming it represents
real-world cancellation behavior.]

### Destination Distribution

[Identify the most frequently recorded destination and its
percentage of all booking records.]

### Booking Channels

[Compare the record counts and percentages across channels.
Do not describe these as conversion rates.]

### Monthly Booking Volume

[Report the highest- and lowest-volume months and their counts.
Explain that random generation may account for the variation.]

### Booking Prices

[Report the median and mean, and briefly describe the
distribution shown in the price histogram.]

## 5. Limitations

- All booking records are synthetic.
- Booking status and destination selection are randomized.
- The dataset contains no website visitor or booking-funnel
  event data, so conversion rates cannot be calculated.
- Booking price is not verified revenue.
- Patterns in this dataset should not be generalized to
  actual travel customers or markets.

## 6. Next Steps

- Query the cleaned data using SQL.
- Create a business-focused dashboard.
- Improve the simulated data model to support more realistic
  analytical questions.
- Document reproducible results and visualizations.

## 7. Tools

Python, pandas, Matplotlib, Seaborn, Git, and GitHub.
