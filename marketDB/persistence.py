import sqlite3
import atexit
from dbtools import Dao
from initiate import Activityreports,Namesaleincomes, Employees, Suppliers, Products, Branches
 
# Data Transfer Objects:

class Employee(object):

    #TODO: implement

    def __init__(self, name, salary, branche):

        self.id= id

        self.name = name

        self.salary = salary

        self.branche = branche



    pass

 

class Supplier(object):

    #TODO: implement

    def __init__(self, id, name, contact_information):

        self.id = id

        self.name = name

        self.contact_information = contact_information

        pass

    pass



class Product(object):

    #TODO: implement

    def __init__(self, id, description, price, quantity):

        self.id = id

        self.description = description

        self.price = price

        self.quantity = quantity

    pass



class Branche(object):

    #TODO: implement

    def __init__(self, id, location, number_of_employees ):

        self.id = id

        self.location = location

        self.number_of_employees  = number_of_employees 

    pass



class Activitie(object):

    #TODO: implement

    def __init__(self, product_id, quantity, activator_id, date):

        self.product_id = product_id

        self.quantity = quantity

        self.activator_id = activator_id

        self.date = date

    pass

class Activityreport(object):

    #TODO: implement

    def __init__(self, date, item_description, quantity, name_seller,name_supplier ):

        self.date = date

        self.item_description = item_description

        self.quantity = quantity

        self.name_seller = name_seller
        
        self.name_supplier = name_supplier

    pass

class Namesaleincome(object):

    #TODO: implement

    def __init__(self,id, name, income ):

        self.id = id

        self.name = name

        self.income = income

   
    pass

 


 
#Repository
class Repository(object):
    def __init__(self):
        self._conn = sqlite3.connect('bgumart.db')
        self._conn.text_factory = bytes
        #TODO: complete
        
        # DAO of the tables
        self.employees = Employees(self._conn)
        self.suppliers = Suppliers(self._conn)
        self.products = Products(self._conn)
        self.branches = Branches(self._conn)
        self.activityreports = Activityreports(self._conn)
        self.namesaleincomes = Namesaleincomes(self._conn)
 
    def _close(self):
        self._conn.commit()
        self._conn.close()
 
    def create_tables(self):
        self._conn.executescript("""
            CREATE TABLE if not exists employees (
                id              INT         PRIMARY KEY,
                name            TEXT        NOT NULL,
                salary          REAL        NOT NULL,
                branche    INT REFERENCES branches(id)
            );
    
            CREATE TABLE if not exists suppliers (
                id                   INTEGER    PRIMARY KEY,
                name                 TEXT       NOT NULL,
                contact_information  TEXT
            );

            CREATE TABLE if not exists products (
                id          INTEGER PRIMARY KEY,
                description TEXT    NOT NULL,
                price       REAL NOT NULL,
                quantity    INTEGER NOT NULL
            );

            CREATE TABLE if not exists branches (
                id                  INTEGER     PRIMARY KEY,
                location            TEXT        NOT NULL,
                number_of_employees INTEGER
            );
    
            CREATE TABLE if not exists activities (
                product_id      INTEGER REFERENCES products(id),
                quantity        INTEGER NOT NULL,
                activator_id    INTEGER NOT NULL,
                date            TEXT    NOT NULL
            );
            
            CREATE TABLE if not exists activities_report (
                date            TEXT    NOT NULL,  
                item_description TEXT   NOT NULL,
                quantity         INTEGER NOT NULL,
                name_seller      TEXT           ,
                name_supplier    TEXT
            );
            
            CREATE TABLE if not exists name_sale_incomes (
                id            INTEGER REFERENCES employees(id),  
                name          TEXT   NOT NULL,
                sale_income   FLOAT NOT NULL
                
            );
            
            
            
        """)

    def execute_command(self, script: str) -> list:
        return self._conn.cursor().execute(script).fetchall()
 
# singleton
repo = Repository()
atexit.register(repo._close)