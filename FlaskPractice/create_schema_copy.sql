-- Schema
--DROP TABLE IF EXISTS students;


CREATE TABLE students (
  id           serial PRIMARY KEY,
  first_name   VARCHAR(255) NOT NULL,
  last_name    VARCHAR(255) NOT NULL,
  age          INT,
  grade        CHAR (1)
);


COPY students FROM 
'/Users/miyapollard/Desktop/sql-basics/data.csv' 
DELIMITER ',' CSV HEADER;

--INSERT INTO students (first_name, last_name, age, grade) VALUES
    -- ('John', 'Doe', 18, 'A'),
    -- ('Jane', 'Smith', 19, 'B'),
    -- ('Bob', 'Johnson', 20, 'A'),
    -- ('Emily', 'Williams', 18, 'A'),
    -- ('Michael', 'Brown', 19, 'B'),
    -- ('Francisco', 'Avila', 39, 'B');

--SELECT * FROM students;