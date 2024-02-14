-- script that lists all cities contained in the database hbtn_0d_usa
--script connects h0d_usa database and executes query to retrieve all cities 
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
