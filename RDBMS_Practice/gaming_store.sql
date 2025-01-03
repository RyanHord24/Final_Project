-- Drop the table if it exists
DROP TABLE IF EXISTS games;

-- Create Games Table
CREATE TABLE games (
    game_id INT PRIMARY KEY,
    game_title VARCHAR(255) UNIQUE,
    quantity INT,
    price DECIMAL(5, 2)
);

-- Drop the table if it exists
DROP TABLE IF EXISTS posters;

-- Create Posters Table
CREATE TABLE posters (
    poster_id INT PRIMARY KEY,
    poster_title VARCHAR(255) UNIQUE,
    quantity INT,
    price DECIMAL(5, 2)
);

-- Drop the table if it exists
DROP TABLE IF EXISTS employees;

-- Create Employees Table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(255) UNIQUE,
    position VARCHAR(255),
    salary DECIMAL(8, 2)
);

-- Drop the table if it exists
DROP TABLE IF EXISTS action_figures;

-- Create Action Figures Table
CREATE TABLE action_figures (
    action_figure_id INT PRIMARY KEY,
    action_figure_title VARCHAR(255) UNIQUE,
    quantity INT,
    price DECIMAL(5, 2)
);