-- script displays top 3 of cities temperature during 7 and 8 ordered tem.
SELECT city, MAX(temperature) AS max_temperature
FROM temperature_data
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY max_temperature DESC
LIMIT 3;
