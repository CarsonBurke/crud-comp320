import sqlite3

def db_client():
    client = sqlite3.connect("data.db")
    return client

def add_employee(name, email, role, manager_id):
    if not name:
        name = input("Enter employee name: ")
    if not email:
        email = input("Enter employee email: ")
    if not role:
        role = input("Enter employee role (Management, Sales, Logistics, Delivery, Finances): ")
    if not manager_id:
        manager_id = input("Enter employee manager id: ")

    client = db_client()
    client.execute("INSERT INTO Employees (name, email, role, manager_id) VALUES (?, ?, ?, ?)", (name, email, role, manager_id))
    client.commit()

def find_warehouse(warehouse_name):
    if not warehouse_name:
        warehouse_name = input("Enter warehouse name: ")
    
    client = db_client()
    warehouse = client.execute("SELECT * FROM Warehouses WHERE name LIKE ?", (f"%{warehouse_name}%",)).fetchone()
    return warehouse

def delete_employee_payment(name):
    if not name:
        name = input("Enter employee name: ")
    
    client = db_client()
    client.execute("DELETE FROM EmployeePayments WHERE EmployeePayments.id = (SELECT id FROM Employees WHERE name = ?)", (name,))
    client.commit()

def sales_volume():
    client = db_client()
    sales = client.execute("SELECT SUM(quantity) FROM Sales").fetchone()[0]
    return sales
    
def sales_by_warehouse(warehouse_name):
    if not warehouse_name: 
        warehouse_name = input("Enter warehouse name: ")
    
    client = db_client()
    sales = client.execute("SELECT COUNT(*), SUM(quantity), SUM(price) FROM Sales JOIN Warehouses ON (Sales.id=Warehouses.id) WHERE Warehouses.name = ?", (warehouse_name,)).fetchone()
    return sales
    
def sales_under_manager(manager_name):
    
    if not manager_name:
        manager_name = input("Enter manager name: ")
    
    client = db_client()
    underlyings_raw = client.execute("SELECT underlings FROM Managers WHERE employee_id = (SELECT id FROM employees WHERE name = ?)", (manager_name,)).fetchone()
    
    underlyings = underlyings_raw[0].split("'")[0].split(",")

    sum = 0
    
    for underlying in underlyings:
        sales = client.execute("SELECT SUM(price) FROM Sales WHERE employee_id = ?", (underlying,)).fetchone()[0]
        sum += sales
    
    return sum

def test():

    # test read warehouse
    try:
        warehouse = find_warehouse("Main Warehouse")
        print("Found test passed; warehouse:", warehouse)
    except Exception as e:
        print(f"Find warehouse function failed: {e}")

    # test add employee
    try:
        add_employee("Luke Cosner", "cosner@gmail.com", "Sales", 2)
        print("Add employee function works")
    except Exception as e:
        print(f"Add employee function failed, employee may already exist: {e}")
        
    # test delete employee payment
    try:
        delete_employee_payment("James Wilson")
        print("Delete employee payment function works")
    except Exception as e:
        print(f"Delete employee payment function failed: {e}")
        
    
    # test sales volume
    try:
        volume = sales_volume()
        print(f"Sales volume: {volume}")
    except Exception as e:
        print(f"Sales volume function failed: {e}")
    
    # test sales by warehouse
    try:
        warehouse = "Main Warehouse"
        sales = sales_by_warehouse(warehouse)
        print(f"Sales for warehouse: {warehouse} (count: {sales[0]}, quantity: {sales[1]}, price: {sales[2]})")
    except Exception as e:
        print(f"Sales by warehouse function failed: {e}")
        
    # test sales under manager
    try:
        manager = "David Miller"
        sum = sales_under_manager(manager)
        print(f"Sales under manager: {manager} {sum}")
    except Exception as e:
        print(f"Sales under manager function failed: {e}")

def crud():
    while True:
        choice = input("Exit: -1\nSelect an option:\n0. Add Employee\n1. Find warehouse\n2. Delete employee payment\n3. Total sales volume\n4. Sales for warehouse\n5. Sales under manager\n")
        
        match choice:
            case "-1":
                break
            case "0":
                add_employee(None, None, None, None)
            case "1":
                sales = find_warehouse(None)
                print(f"Warehouse sales: (count: {sales[0]}, quantity: {sales[1]}, price: {sales[2]})")
            case "2":
                delete_employee_payment(None)
            case "3":
                print(sales_volume())
            case "4":
                print(sales_by_warehouse(None))
            case "5":
                print(sales_under_manager(None))
            

crud()