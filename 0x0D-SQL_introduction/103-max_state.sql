-- script displays max temperature of each state (ordered by State name).
SELECT state, MAX(value) AS max_temperature
FROM temperature_data
GROUP BY state
ORDER BY state;
