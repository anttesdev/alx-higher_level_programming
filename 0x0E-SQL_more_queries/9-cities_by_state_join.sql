-- Selects all cities along with their corresponding state names and orders them by city ID.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
