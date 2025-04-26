CREATE TABLE Warehouses (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL,
 address TEXT NOT NULL
);

CREATE TABLE Customers (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL,
 email TEXT UNIQUE NOT NULL,
 phone TEXT NOT NULL
);

CREATE TABLE Employees (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL,
 email TEXT UNIQUE NOT NULL,
 role TEXT NOT NULL,
 manager_id INTEGER NOT NULL,
 FOREIGN KEY (manager_id) REFERENCES Employees(id)
);

-- One to many relationship with employees
CREATE TABLE Managers (
 employee_id INTEGER PRIMARY KEY,
 -- Employees that the manager directly oversees
 underlings TEXT NOT NULL,
 FOREIGN KEY (employee_id) REFERENCES Employees(id)
);

-- One to one relationship with employee
CREATE TABLE EmployeePayments (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 date TEXT NOT NULL,
 employee_id INTEGER NOT NULL,
 amount INTEGER NOT NULL,
 FOREIGN KEY (employee_id) REFERENCES Employees(id)
);

CREATE TABLE Products (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL,
 price INTEGER NOT NULL,
 amount INTEGER NOT NULL,
 warehouse_id INTEGER NOT NULL
);

-- One to one relationship with warehouse
CREATE TABLE Sales (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 customer_id INTEGER NOT NULL,
 product_id INTEGER NOT NULL,
 -- The employee who sold the product
 employee_id INTEGER NOT NULL,
 quantity INTEGER NOT NULL,
 price INTEGER NOT NULL,
 completed BOOLEAN NOT NULL,
 warehouse_id INTEGER NOT NULL,
 FOREIGN KEY (customer_id) REFERENCES Customers(id),
 FOREIGN KEY (warehouse_id) REFERENCES Warehouses(id)
);