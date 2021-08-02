import sqlite3
from sqlite3.dbapi2 import connect

def createTable():
    connectors = sqlite3.connect("lite.db")
    cursor  = connectors.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quanlity INTERGER,price REAL)")
    connectors.commit()
    connectors.close()

def insert(item,quanlity,price):
    connectors = sqlite3.connect("lite.db")
    cursor  = connectors.cursor()
    cursor.execute("INSERT INTO store VALUES(?,?,?)",(item,quanlity,price))
    connectors.commit()
    connectors.close()

def view():
    connectors = sqlite3.connect("lite.db")
    cursor  = connectors.cursor()
    cursor.execute("SELECT * FROM store")
    row = cursor.fetchall()
    connectors.close()
    return row

def delete(item):
    connectors = sqlite3.connect("lite.db")
    cursor  = connectors.cursor()
    cursor.execute("DELETE FROM store WHERE item=?",(item,))
    connectors.commit()
    connectors.close()

def update(item,quanlity,price):
    connectors = sqlite3.connect("lite.db")
    cursor  = connectors.cursor()
    cursor.execute("UPDATE store SET quanlity=?,price=? WHERE item=?",(quanlity,price,item))
    connectors.commit()
    connectors.close()
#delete('Coca')
update("Fanta",10,19.6)
print(view())