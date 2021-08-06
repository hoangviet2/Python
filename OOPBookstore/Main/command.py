from tkinter import *
from backed import Database
database = Database("books.db")
class commands:
    def __init__(self) -> None:
        print("Hi command")
    def delete_comd(self):
        database.delete(selected_Tupple[0])

    def update_comd(self,listOfEntry):
        database.update(selected_Tupple[0],listOfEntry[0].get(),listOfEntry[1].get(),listOfEntry[2].get(),listOfEntry[3].get())

    def get_select_row(event,self,listBoxs,listOfEntry):
        try:
            global selected_Tupple
            index = listBoxs.curselection()[0]
            selected_Tupple = listBoxs.get(index)
            listOfEntry[0].delete(0,END)
            listOfEntry[0].insert(END,selected_Tupple[1])
            listOfEntry[1].delete(0,END)
            listOfEntry[1].insert(END,selected_Tupple[2])
            listOfEntry[2].delete(0,END)
            listOfEntry[2].insert(END,selected_Tupple[3])
            listOfEntry[3].delete(0,END)
            listOfEntry[3].insert(END,selected_Tupple[4])
        except IndexError:
            pass

    def view_All_comd(self,listBoxs):
        listBoxs.delete(0,END)
        for book in database.view():
            listBoxs.insert(END,book)

    def search_comd(self,listBoxs):
        listBoxs.delete(0,END)
        for row in database.search(title=listBoxs[0].get(),author=listBoxs[1].get(),year=listBoxs[2].get(),isbn=listBoxs[3].get()):
            listBoxs.insert(END,row)

    def add_comd(self,listBoxs,listOfEntry):
        database.insert(listOfEntry[0].get(),listOfEntry[1].get(),listOfEntry[2].get(),listOfEntry[3].get())
        listBoxs.delete(0,END)
        listBoxs.insert(END,(listOfEntry[0].get(),listOfEntry[1].get(),listOfEntry[2].get(),listOfEntry[3].get()))
