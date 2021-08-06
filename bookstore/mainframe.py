from tkinter import *
from backed import Database
database = Database()
window = Tk()
window.wm_title("Book store")

def delete_comd():
    database.delete(selected_Tupple[0])

def update_comd():
    database.update(selected_Tupple[0],titleEntry.get(),authorEntry.get(),yearEntry.get(),ISBNEntry.get())

def get_select_row(event):
    try:
        global selected_Tupple
        index = listBox.curselection()[0]
        selected_Tupple = listBox.get(index)
        titleEntry.delete(0,END)
        titleEntry.insert(END,selected_Tupple[1])
        authorEntry.delete(0,END)
        authorEntry.insert(END,selected_Tupple[2])
        yearEntry.delete(0,END)
        yearEntry.insert(END,selected_Tupple[3])
        ISBNEntry.delete(0,END)
        ISBNEntry.insert(END,selected_Tupple[4])
    except IndexError:
        pass

def view_All_comd():
    listBox.delete(0,END)
    for book in database.view():
        listBox.insert(END,book)

def search_comd():
    listBox.delete(0,END)
    for row in database.search(title=titleEntry.get(),author=authorEntry.get(),year=yearEntry.get(),isbn=ISBNEntry.get()):
        listBox.insert(END,row)

def add_comd():
    database.insert(titleEntry.get(),authorEntry.get(),yearEntry.get(),ISBNEntry.get())
    listBox.delete(0,END)
    listBox.insert(END,(titleEntry.get(),authorEntry.get(),yearEntry.get(),ISBNEntry.get()))

#title label,Entry
title_lb = Label(window,text="title")
title_lb.grid(row=0,column=0)

titleEntryValue = StringVar()
titleEntry = Entry(window,textvariable=titleEntryValue)
titleEntry.grid(row=0,column=1)

#Year label
year_lb = Label(window,text="year")
year_lb.grid(row=1,column=0)

yearEntryValue = StringVar()
yearEntry = Entry(window,textvariable=yearEntryValue)
yearEntry.grid(row=0,column=3)

#author label
author_lb = Label(window,text="author")
author_lb.grid(row=0,column=2)

authorEntryValue = StringVar()
authorEntry = Entry(window,textvariable=authorEntryValue)
authorEntry.grid(row=1,column=1)

#ISBN label
ISBN_lb = Label(window,text="ISBN")
ISBN_lb.grid(row=1,column=2)

ISBNEntryValue = StringVar()
ISBNEntry = Entry(window,textvariable=ISBNEntryValue)
ISBNEntry.grid(row=1,column=3)

#list box
listBox = Listbox(window,height=6,width=35)
listBox.grid(row=2,column=0,rowspan=6,columnspan=2)

listBox.bind('<<ListboxSelect>>',get_select_row)

#Scroll bar
scrollBar = Scrollbar(window)
scrollBar.grid(row=2,column=2,rowspan=6)

listBox.configure(yscrollcommand=scrollBar.set)
scrollBar.configure(command=listBox.yview)

#button
button_ViewAll = Button(window,text="View All",width=20,command=view_All_comd)
button_ViewAll.grid(row=2,column=3)

button_SearchEntry = Button(window,text="Search Entry",width=20,command=search_comd)
button_SearchEntry.grid(row=3,column=3)

button_AddEntry = Button(window,text="Add Entry",width=20,command= add_comd)
button_AddEntry.grid(row=4,column=3)

button_Update = Button(window,text="Update",width=20,command=update_comd)
button_Update.grid(row=5,column=3)

button_Delete = Button(window,text="Delete",width=20,command=delete_comd)
button_Delete.grid(row=6,column=3)

button_Close = Button(window,text="Close",width=20,command=window.destroy)
button_Close.grid(row=7,column=3)

window.mainloop()