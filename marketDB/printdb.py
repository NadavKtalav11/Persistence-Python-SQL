from persistence import *
from initiate import *

def main():
    
    databaseexisted = os.path.isfile('bgumart.db')
    dbcon = sqlite3.connect('bgumart.db')
    with dbcon:
        cursor = dbcon.cursor()
        cursor.execute("SELECT * FROM activities ORDER BY date ASC");
        activities_table = cursor.fetchall()
        print("Activities")
        for activite in activities_table:
            print (str(activite))
        pass
    
        cursor.execute("SELECT * FROM branches ORDER BY id ASC");
        branches_table = cursor.fetchall()
        print("Branches")
        for branche in branches_table:
            print (str(branche))
        pass
    
        cursor.execute("SELECT * FROM employees ORDER BY id ASC");
        employees_table = cursor.fetchall()
        print("Employees")
        for employees in employees_table:
            print (str(employees))
        pass
    
        cursor.execute("SELECT * FROM products ORDER BY id ASC");
        products_table = cursor.fetchall()
        print("Products")
        for product in products_table:
            print (str(product))
        pass
    
        cursor.execute("SELECT * FROM suppliers ORDER BY id ASC");
        suppliers_table = cursor.fetchall()
        print("Suppliers")
        for supplier in suppliers_table:
            print (str(supplier))
        pass
    
        print("Employees report")
        cursor.execute("SELECT employees.name, employees.salary, branches.location, name_sale_incomes.sale_income FROM employees JOIN branches ON employees.branche =branches.id JOIN name_sale_incomes ON name_sale_incomes.id =employees.id ORDER BY employees.name ASC");
        employees_report = cursor.fetchall()
        for employees_report1 in employees_report:
            if employees_report1[-1]+0 == 0:
                print (*employees_report1[0:-1], 0)
            else: 
                print(*employees_report1)
        
        
        cursor.execute("SELECT * FROM activities_report ORDER BY date ASC");
        activities_report_table = cursor.fetchall()
        print("Activities report")
        for activities_report in activities_report_table:
            print (str(activities_report))
        pass

if __name__ == '__main__':
    main() 