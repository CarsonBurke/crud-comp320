# Term Project Carson Burke

A Basic CRUD application programmed from the ground up using a custom schema, to showcase knowledge of SQL and its usage in websites and applications with middleware.

## Core Entities

- Warehouses: Storage locations for products
- Products: Items sold by the company, each associated with a specific warehouse
- Customers: Clients that purchase products
- Sales: Transaction records linking customers, products, commissinoed employees and warehouses
- Employees: Staff members with info, roles and manager
- Managers: Manager-specific information such as who they oversee
- EmployeePayments: Payroll history for employee compensation

## Getting Started

1. Clone the repository
2. Install dependencies: `sqlite3`
3. Initialize the application using the schema: `sqlite3 data.db < schema.sql`
4. Run the CRUD CLI application: `py app.py`

## Entity-Relationship Diagram (Mermaid.js)

```mermaid
erDiagram Warehouses ||--o{ Products : "stores" Warehouses ||--o{ Sales : "supplies_from" Customers ||--o{ Sales : "places" Products ||--o{ Sales : "included_in" Employees ||--o{ Sales : "sells" Employees ||--o{ EmployeePayments : "receives" Employees ||--o{ Employees : "manages" Employees ||--|| Managers : "is_a" Warehouses { integer id PK text name text address } Customers { integer id PK text name text email text phone } Employees { integer id PK text name text email text role integer manager_id FK } Managers { integer employee_id PK,FK text underlings } EmployeePayments { integer id PK text date integer employee_id FK integer amount } Products { integer id PK text name integer price integer amount integer warehouse_id FK } Sales { integer id PK integer customer_id FK integer product_id FK integer employee_id FK integer quantity integer price boolean completed integer warehouse_id FK }
```

