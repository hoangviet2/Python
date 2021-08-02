import sqlite3
from sqlite3.dbapi2 import Cursor

def connect():
    connectors = sqlite3.connect("books.db")
    cursor = connectors.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year text,isbn integer)")
    connectors.commit()
    connectors.close()

def insert(title,author,year,isbn):
    connectors = sqlite3.connect("books.db")
    cursor  = connectors.cursor()
    cursor.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    connectors.commit()
    connectors.close()

def view():
    connectors = sqlite3.connect("books.db")
    cursor  = connectors.cursor()
    cursor.execute("SELECT * FROM books")
    row = cursor.fetchall()
    connectors.close()
    return row

def search(title = "",author = "",year="",isbn=""):
    connectors = sqlite3.connect("books.db")
    cursor  = connectors.cursor()
    cursor.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR isbn = ? ",(title,author,year,isbn))
    row = cursor.fetchall()
    connectors.close()
    return row

def delete(id):
    connectors = sqlite3.connect("books.db")
    cursor  = connectors.cursor()
    cursor.execute("DELETE FROM books WHERE id =?",(id,))
    connectors.commit()
    connectors.close()

def update(id,title,author,year,isbn):
    connectors = sqlite3.connect("books.db")
    cursor  = connectors.cursor()
    cursor.execute("UPDATE books SET title=?,author=?,year=?,isbn=? WHERE id=?",(id,title,author,year,isbn))
    connectors.commit()
    connectors.close()

connect()
print(view())