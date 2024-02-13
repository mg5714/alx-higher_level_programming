-- script that displays average temperature by city ordered by temperature.
SELECT city, AVG(temperature) AS average_temperature_fahrenheit
FROM temperature_data
GROUP BY city
ORDER BY average_temperature_fahrenheit DESC;
