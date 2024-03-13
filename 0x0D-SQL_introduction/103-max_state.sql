-- Retrieves the maximum temperature recorded for each state, ordered alphabetically by state name
SELECT state, MAX(temperature) AS max_temperature
FROM temperatures
GROUP BY state
ORDER BY state;
