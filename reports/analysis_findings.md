
# Travel Booking & Customer Journey Analytics

## 1. Project Overview

This project explores a synthetic travel-booking dataset using
Python and pandas. The analysis covers data quality, booking
status, destination distribution, booking channels, monthly
booking volume, and booking-price distribution.

## 2. Dataset Description

- Records analyzed: 1000
- Unique customers: 289
- Destinations represented: 8
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

The synthetic travel-booking dataset contains 1,000 booking records, distributed across three booking statuses:

- **Confirmed:** 570 bookings (57.0%)
- **Completed:** 225 bookings (22.5%)
- **Cancelled:** 205 bookings (20.5%)

**Key Finding:** Confirmed bookings represent the largest proportion of records at 57.0%, followed by completed bookings at 22.5% and cancelled bookings at 20.5%.

**Business Interpretation:** Booking status distribution is useful for monitoring booking outcomes and identifying records requiring further investigation. However, because this dataset is synthetically generated, these percentages should not be interpreted as real-world customer cancellation or completion behavior.

### Destination Distribution

The synthetic travel-booking dataset contains 1,000 bookings across 8 destinations.

| Destination | Number of Bookings | Percentage |
|---|---:|---:|
| Paris | 143 | 14.3% |
| Dubai | 142 | 14.2% |
| Rome | 133 | 13.3% |
| Singapore | 121 | 12.1% |
| New York | 119 | 11.9% |
| Sydney | 118 | 11.8% |
| London | 115 | 11.5% |
| Tokyo | 109 | 10.9% |
| **Total** | **1,000** | **100.0%** |

**Key Finding:** Paris was the most frequently recorded destination, with 143 bookings (14.3%), followed closely by Dubai with 142 bookings (14.2%). Tokyo had the lowest booking count, with 109 bookings (10.9%).

**Business Interpretation:** Destination distribution analysis can help travel companies identify popular destinations and plan marketing activities. However, the differences in this synthetic dataset should not be interpreted as evidence of real-world travel preferences.

### Booking Channels

The dataset contains bookings from three different channels.

| Booking Channel | Number of Bookings | Percentage |
|---|---:|---:|
| Mobile App | 356 | 35.6% |
| Travel Agent | 340 | 34.0% |
| Website | 304 | 30.4% |
| **Total** | **1,000** | **100.0%** |

**Key Finding:** Mobile App accounted for the largest proportion of bookings at 35.6%, followed by Travel Agent at 34.0% and Website at 30.4%.

**Business Interpretation:** Booking channel analysis can help businesses understand how recorded bookings are distributed across platforms and intermediaries. These percentages represent shares of bookings, not conversion rates, because the dataset does not include visitor counts or booking attempts.

### Monthly Booking Volume

Booking volume was analyzed using the `booking_date` column. The dataset covers January 2024 through December 2025.

| Metric | Month | Number of Bookings |
|---|---|---:|
| Highest booking volume | April 2024 | 52 |
| Lowest booking volume (tie) | January 2024 | 31 |
| Lowest booking volume (tie) | November 2025 | 31 |

**Key Finding:** April 2024 recorded the highest booking volume with 52 bookings. January 2024 and November 2025 tied for the lowest booking volume, with 31 bookings each. The difference between the highest and lowest monthly counts was 21 bookings.

**Business Interpretation:** Monthly booking analysis can help businesses monitor demand fluctuations, identify potential seasonal patterns, and plan staffing or marketing activities. Because this dataset was randomly generated, these differences may reflect the data-generation process rather than genuine seasonal travel demand.

### Booking Prices

Booking prices were analyzed to understand their central tendency, range, and distribution.

| Price Metric | Value |
|---|---:|
| Mean Booking Price | $991.28 |
| Median Booking Price | $785.17 |
| Minimum Booking Price | $180.97 |
| Maximum Booking Price | $2,698.19 |
| 25th Percentile | $382.09 |
| 75th Percentile | $1,498.23 |

**Key Finding:** The average booking price was $991.28, while the median was $785.17. The mean was approximately $206.11 higher than the median, suggesting that relatively high-priced bookings pull the average upward. This is consistent with a potentially right-skewed price distribution, although the histogram should be inspected to confirm its shape.

The middle 50% of booking prices fell between $382.09 and $1,498.23.

**Business Interpretation:** Booking price analysis can help travel companies understand pricing variation, develop price-based customer segments, and support revenue reporting. However, the observed price distribution comes from synthetic data and should not be treated as representative of real travel-market prices.
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
