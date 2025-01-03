-- Drop the table if it exists
DROP TABLE IF EXISTS inventory;

-- Create Inventory Table
CREATE TABLE inventory (
    id INT PRIMARY KEY,
    item_name VARCHAR(255) UNIQUE,
    item_type VARCHAR(255),
    quantity BIGINT,
    price DECIMAL(8, 2)
);

-- Drop the table if it exists
DROP TABLE IF EXISTS sales;

-- Create Sales Table
CREATE TABLE sales (
    id INT PRIMARY KEY,
    menu_option VARCHAR(255) UNIQUE,
    ice_cream_flavor VARCHAR(255),
    cone_flavor VARCHAR(255),
    sale_cost DECIMAL(8, 2),
    amount_of_sales BIGINT
);

-- Drop the table if it exists
DROP TABLE IF EXISTS employees;

-- Create Employees Table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(255) UNIQUE,
    position VARCHAR(255),
    hours_worked DECIMAL(8, 2),
    sales_made BIGINT
);