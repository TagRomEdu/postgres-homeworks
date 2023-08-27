-- SQL-команды для создания таблиц

CREATE TABLE employees
(
	employee_id varchar(100) PRIMARY KEY,
	first_name varchar(50),
	last_name varchar(50),
	title varchar(100),
	birth_date varchar(100),
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(100) PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100)
);

CREATE TABLE orders
(
	order_id varchar(100) PRIMARY KEY,
	customer_id varchar(100) REFERENCES customers(customer_id),
	employee_id varchar(100) REFERENCES employees(employee_id),
	order_date varchar(100),
	ship_city varchar(50)
);