-- Import the table dump into the hbtn_0c_0 database

-- Write a script to display the average temperature by city in Fahrenheit
SELECT city, AVG(temperature * 9/5 + 32) AS avg_temperature_fahrenheit
FROM weather_data
GROUP BY city
ORDER BY avg_temperature_fahrenheit DESC;
