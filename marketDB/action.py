from persistence import *
from typing import List
import sys
from initiate import *

 



def main(args : List[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            #TODO: apply the action (and insert to the table) if possible
            if int(splittedline[1]) > 0:
                updateSupplyActivity(splittedline)
                
            elif int(splittedline[1]) < 0:
                updateSaleActivity(splittedline)
            

                
def updateSupplyActivity(splittedline: List[str]):
    dbcon = sqlite3.connect('bgumart.db')
    with dbcon:
        cursor = dbcon.cursor()
        
    amount =cursor.execute("SELECT * FROM products where id = (?)", [splittedline[0]])
    curr_qua_int = amount.fetchall()
    lista = curr_qua_int.pop()
    curr_amount = int(lista[3])
    
    repo._conn.execute("INSERT INTO activities  VALUES (?,?, ?,?)", (splittedline[0], splittedline[1], splittedline[2], splittedline[3]))
    supply_amount = int(splittedline[1])
    newamount= curr_amount +supply_amount
    repo._conn.execute("UPDATE products SET quantity = (?) WHERE id = (?)", [newamount, int(splittedline[0])])
    
    item_description = cursor.execute("SELECT * FROM products where id = (?)", [splittedline[0]])
    description  = item_description.fetchall()
    listb = description.pop()
    
    name_supplier = cursor.execute("SELECT * FROM suppliers where id = (?)", [splittedline[2]])
    name_q = name_supplier.fetchall()
    listc = name_q.pop()
    
    list5 = [splittedline[3],splittedline[1]]
    name_seller = None
    repo._conn.execute("INSERT INTO activities_report  VALUES (?,?, ?, ?, ?)", [splittedline[3], listb[1] ,int(splittedline[1]), name_seller, str(listc[1])])
    
    pass 

def updateSaleActivity(splittedline: List[str]):
    dbcon = sqlite3.connect('bgumart.db')
    with dbcon:
        cursor = dbcon.cursor()
    amount = repo._conn.execute("SELECT * FROM products where id = (?)", (splittedline[0]))
    curr_qua_int = amount.fetchall()
    lista = curr_qua_int.pop()
  
   
    if  lista[3] >= (int(splittedline[1]) *-1):
        repo._conn.execute("INSERT INTO activities  VALUES (?,?, ?,?)", (splittedline[0], splittedline[1], splittedline[2], splittedline[3]))
        newamount = int(splittedline[1])+int(lista[3])
        repo._conn.execute("UPDATE products SET quantity =   (?)   where id =(?)", [newamount, splittedline[0]])
        item_description = cursor.execute("SELECT * FROM products where id = (?)", [splittedline[0]])
        description  = item_description.fetchall()
        listb = description.pop()
        
        name_seller = cursor.execute("SELECT * FROM employees where id = (?)", [splittedline[2]])
        name_s = name_seller.fetchall()
        listc = name_s.pop()
        
        
        list5 = [splittedline[3],splittedline[1]]
        name_supplier = None
        repo._conn.execute("INSERT INTO activities_report  VALUES (?,?, ?, ?, ?)", (list5[0], str(listb[1]), list5[1], str(listc[1]), name_supplier))
                
        productPrice = cursor.execute("SELECT * FROM products where id = (?)", [splittedline[0]])
        price = productPrice.fetchall()
        listd = price.pop()
        p_price = float(listd[2])
        extra_amount = float(splittedline[1]) * float(-1)
        incereseIncomeBy = extra_amount * p_price
        update_name_saleIncomes(splittedline[2], incereseIncomeBy)
    

        pass  
    

def update_name_saleIncomes(idEmpl, incerseIncome):
    dbcon = sqlite3.connect('bgumart.db')
    with dbcon:
        cursor = dbcon.cursor()
    current_income = cursor.execute("SELECT * FROM name_sale_incomes where id = (?)",  [idEmpl])
    salary = current_income.fetchall()
    list89 = salary.pop()
    currentincome1 = float(list89[2])
    newIncome =  float(currentincome1) + float(incerseIncome)
    repo._conn.execute("UPDATE name_sale_incomes SET sale_income = sale_income + (?) where id = (?)", [newIncome, idEmpl])
    
    pass


           
    

       

if __name__ == '__main__':
    main(sys.argv)