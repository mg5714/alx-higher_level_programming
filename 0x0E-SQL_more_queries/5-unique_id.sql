-- script that creates the table unique_id on your MySQL server.
-- Check if the table unique_id already exists, and if not, create it
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
