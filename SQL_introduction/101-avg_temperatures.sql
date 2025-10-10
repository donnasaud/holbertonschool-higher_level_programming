-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)

SELECT city, AVG(value) avg_temp
-- avg_temp is an alias (nickname) for the average,
-- so the result column will be labeled avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
