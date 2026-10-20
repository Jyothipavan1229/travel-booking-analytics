# SQL Analysis Findings — Travel Booking Analytics

## Project Overview
SQL was used to analyze the cleaned travel-booking dataset stored in a SQLite database.

## SQL Techniques Used
- SELECT and WHERE
- GROUP BY and ORDER BY
- COUNT, SUM, AVG, MIN, and MAX
- DISTINCT and HAVING
- Subqueries
- Date functions using `strftime()` and `julianday()`
- Data quality checks

## Key Analysis Areas

### Booking Status
Analyzed the distribution of confirmed, cancelled, and completed bookings.

### Destination Analysis
Compared booking volume and average booking prices across destinations.

### Booking Channel Analysis
Compared booking counts and average prices for the website, mobile app, and travel-agent channels.

### Pricing Analysis
Calculated average, minimum, maximum, and total recorded booking values.

### Monthly Trends
Analyzed booking volume by month and booking status.

### Data Quality
Checked for duplicate booking IDs, invalid prices, and missing values in important columns.

## Limitations
- The dataset contains synthetic records.
- Booking patterns do not represent actual travel-market behavior.
- Recorded booking prices are not verified revenue.
- The dataset does not include website visits or funnel events, so conversion rates cannot be calculated.

## Tools Used
Python, pandas, SQLite, SQL, Matplotlib, Seaborn, and Visual Studio Code.

## Conclusion
This project demonstrates a data analysis workflow covering data inspection, cleaning, exploratory analysis, visualization, database creation, and SQL-based business questions.