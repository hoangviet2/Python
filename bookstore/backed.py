import sqlite3
from sqlite3.dbapi2 import Cursor, DatabaseError

class Database:
    def __init__(self):
        self.connectors = sqlite3.connect("books.db")
        self.cursor = self.connectors.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year text,isbn integer)")
        self.connectors.commit()
        
    
    def insert(self,title,author,year,isbn):
        self.cursor.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self.connectors.commit()

    def view(self):
        self.cursor.execute("SELECT * FROM books")
        row = self.cursor.fetchall()
        return row

    def search(self,title = "",author = "",year="",isbn=""):
        self.cursor.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR isbn = ? ",(title,author,year,isbn))
        row = self.cursor.fetchall()
        return row

    def delete(self,id):
        self.cursor.execute("DELETE FROM books WHERE id =?",(id,))
        self.connectors.commit()

    def update(self,id,title,author,year,isbn):
        self.cursor.execute("UPDATE books SET title=?,author=?,year=?,isbn=? WHERE id=?",(id,title,author,year,isbn))
        self.connectors.commit()