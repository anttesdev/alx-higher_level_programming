-- Retrieve all cities of California from the database hbtn_0d_usa, sorted by cities.id
SELECT *
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
