--script connects h0d_usa database and executes query to retrieve all cities
SELECT cities.id AS id, cities.name AS name, states.name AS name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
