from tkinter import *
import backed

window = Tk()

def view_All_comd():
    listBox.delete(0,END)
    for book in backed.view():
        listBox.insert(END,book)

def search_comd():
    listBox.delete(0,END)
    for row in backed.search(title=titleEntry.get(),author=authorEntry.get(),year=yearEntry.get(),isbn=ISBNEntry.get()):
        listBox.insert(END,row)

def add_comd():
    backed.insert(titleEntry.get(),authorEntry.get(),yearEntry.get(),ISBNEntry.get())
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

button_Update = Button(window,text="Update",width=20)
button_Update.grid(row=5,column=3)

button_Delete = Button(window,text="Delete",width=20)
button_Delete.grid(row=6,column=3)

button_Close = Button(window,text="Close",width=20)
button_Close.grid(row=7,column=3)

window.mainloop()