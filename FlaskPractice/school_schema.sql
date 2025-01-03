DROP TABLE IF EXISTS students;

CREATE TABLE students (
  id           serial PRIMARY KEY,
  first_name   VARCHAR(255) NOT NULL,
  last_name    VARCHAR(255) NOT NULL,
  age          INT,
  subject      INT
);

COPY students FROM 
'/Users/miyapollard/Desktop/FlaskPractice/student.csv' 
DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS subjects;

CREATE TABLE subjects (
  id           serial PRIMARY KEY,
  subject      VARCHAR(255) NOT NULL
);

COPY subjects FROM 
'/Users/miyapollard/Desktop/FlaskPractice/subjects.csv' 
DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS teachers;

CREATE TABLE teachers (
  id           serial PRIMARY KEY,
  first_name   VARCHAR(255) NOT NULL,
  last_name    VARCHAR(255) NOT NULL,
  age          INT,
  subject      INT
);

COPY teachers FROM 
'/Users/miyapollard/Desktop/FlaskPractice/teachers.csv' 
DELIMITER ',' CSV HEADER;

