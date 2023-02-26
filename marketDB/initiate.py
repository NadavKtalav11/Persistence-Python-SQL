from persistence import *

import sys
import os
#from typing import List

class Branches:
    def __init__(self,conn):
        self.conn=conn
        pass
    
    def add_branche(splittedline : list):
        #TODO: add the branch into the repo
        repo._conn.execute("INSERT INTO branches  VALUES (?,?, ?)", (splittedline[0], splittedline[1], splittedline[2]))
        pass
     
     
class Suppliers:
    def __init__(self,conn):
        self.conn=conn
        pass     

    def add_supplier(splittedline : list):
        #TODO: insert the supplier into the repo
        repo._conn.execute("INSERT INTO suppliers  VALUES (?,?, ?)", (splittedline[0], splittedline[1], splittedline[2]))
        pass


class Products:
    def __init__(self,conn):
        self.conn=conn
        pass    

    def add_product(splittedline : list):
        #TODO: insert product
        repo._conn.execute("INSERT INTO products  VALUES (?,?,?, ?)", (splittedline[0], splittedline[1], splittedline[2], splittedline[3]))
        pass

class Employees:
    def __init__(self,conn):
        self.conn=conn
        pass 

    def add_employee(splittedline : list):
        #TODO: insert employee
        repo._conn.execute("INSERT INTO employees  VALUES (?,?, ?, ?)", (splittedline[0], splittedline[1], splittedline[2], splittedline[3]))
        zero = 0.0
        Namesaleincomes.add_name_sale_incomes(splittedline[0],splittedline[1],zero)
        pass
    
class Activityreports:
    def __init__(self,conn):
        self.conn=conn
        pass 

    def add_activities_report(splittedline : list, description, seller_name, supplier_name):
        #TODO: insert employee
        repo._conn.execute("INSERT INTO activities_report  VALUES (?,?, ?, ?, ?)", (splittedline[0], description, splittedline[1], seller_name, supplier_name))
        pass
    
class Namesaleincomes:
    def __init__(self,conn):
        self.conn=conn
        pass 

    def add_name_sale_incomes(id,name, income):
        #TODO: insert employee
        repo._conn.execute("INSERT INTO name_sale_incomes  VALUES ( ?, ?, ?)", (id, name, income))
        pass    

adders = {  "B": Branches.add_branche,
            "S": Suppliers.add_supplier,
            "P": Products.add_product,
            "E": Employees.add_employee}

def main(args : list):
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    # uncomment if needed
    if os.path.isfile("bgumart.db"):
         os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])

if __name__ == '__main__':
    main(sys.argv)