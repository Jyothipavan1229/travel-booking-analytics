SELECT *
FROM bookings
LIMIT 10;


SELECT
    COUNT(*) AS total_bookings
FROM bookings;


SELECT
    COUNT(DISTINCT customer_id) AS unique_customers,
    COUNT(DISTINCT destination) AS unique_destinations
FROM bookings;


SELECT
    booking_status,
    COUNT(*) AS total_bookings,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM bookings),
        2
    ) AS percentage_of_bookings
FROM bookings
GROUP BY booking_status
ORDER BY total_bookings DESC;


SELECT
    destination,
    COUNT(*) AS total_bookings,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM bookings),
        2
    ) AS percentage_of_bookings,
    ROUND(AVG(booking_price), 2) AS average_booking_price
FROM bookings
GROUP BY destination
ORDER BY total_bookings DESC;


SELECT
    booking_channel,
    COUNT(*) AS total_bookings,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM bookings),
        2
    ) AS percentage_of_bookings,
    ROUND(AVG(booking_price), 2) AS average_booking_price
FROM bookings
GROUP BY booking_channel
ORDER BY total_bookings DESC;


SELECT
    ROUND(AVG(booking_price), 2) AS average_price,
    MIN(booking_price) AS minimum_price,
    MAX(booking_price) AS maximum_price,
    ROUND(SUM(booking_price), 2) AS total_recorded_booking_value
FROM bookings;


SELECT
    travel_class,
    COUNT(*) AS total_bookings,
    ROUND(AVG(booking_price), 2) AS average_price,
    MIN(booking_price) AS minimum_price,
    MAX(booking_price) AS maximum_price
FROM bookings
GROUP BY travel_class
ORDER BY average_price DESC;


SELECT
    strftime('%Y-%m', booking_date) AS booking_month,
    COUNT(*) AS total_bookings
FROM bookings
GROUP BY strftime('%Y-%m', booking_date)
ORDER BY booking_month;


SELECT
    strftime('%Y-%m', booking_date) AS booking_month,
    booking_status,
    COUNT(*) AS total_bookings
FROM bookings
GROUP BY
    strftime('%Y-%m', booking_date),
    booking_status
ORDER BY booking_month, booking_status;


SELECT
    travel_class,
    destination,
    COUNT(*) AS total_bookings
FROM bookings
GROUP BY travel_class, destination
ORDER BY travel_class, total_bookings DESC;


SELECT
    booking_channel,
    booking_status,
    COUNT(*) AS total_bookings
FROM bookings
GROUP BY booking_channel, booking_status
ORDER BY booking_channel, total_bookings DESC;


SELECT
    ROUND(
        AVG(julianday(travel_date) - julianday(booking_date)),
        1
    ) AS average_days_between_booking_and_travel
FROM bookings;


SELECT
    booking_id,
    COUNT(*) AS occurrences
FROM bookings
GROUP BY booking_id
HAVING COUNT(*) > 1;


SELECT *
FROM bookings
WHERE booking_price IS NULL
   OR booking_price <= 0;


SELECT
    strftime('%Y', booking_date) AS booking_year,
    COUNT(*) AS total_bookings,
    ROUND(AVG(booking_price), 2) AS average_booking_price
FROM bookings
GROUP BY strftime('%Y', booking_date)
ORDER BY booking_year;


SELECT
    destination,
    COUNT(*) AS total_bookings,
    ROUND(SUM(booking_price), 2) AS total_recorded_booking_value
FROM bookings
GROUP BY destination
ORDER BY total_recorded_booking_value DESC
LIMIT 5;


SELECT
    COUNT(*) AS completed_bookings,
    ROUND(AVG(booking_price), 2) AS average_price_of_completed_bookings,
    ROUND(SUM(booking_price), 2) AS total_recorded_value
FROM bookings
WHERE booking_status = 'Completed';


SELECT
    COUNT(*) AS cancelled_bookings,
    ROUND(AVG(booking_price), 2) AS average_price_of_cancelled_bookings
FROM bookings
WHERE booking_status = 'Cancelled';


SELECT
    COUNT(*) AS total_records,
    COUNT(booking_id) AS non_null_booking_ids,
    COUNT(customer_id) AS non_null_customer_ids,
    COUNT(booking_date) AS non_null_booking_dates,
    COUNT(travel_date) AS non_null_travel_dates,
    COUNT(booking_price) AS non_null_prices
FROM bookings;