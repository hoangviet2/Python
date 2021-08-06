from tkinter import *

class UILibary:

    def __init__(self) -> None:
        print("OBject created")

    def create_label(self,corrdinate,content,window):
        print("Created Label")
        label = Label(window,text=content)
        label.grid(row=corrdinate[0],column=corrdinate[1])
        return label

    def create_entry(self,corrdinate,window):
        print("Created Entry")
        textEntry = StringVar()
        entry = Entry(window,textvariable=textEntry)
        entry.grid(row=corrdinate[0],column=corrdinate[1])
        return entry

    def create_boxList(self,corrdinate,size,window,span):
        print("Created a BoxList")
        listBox = Listbox(window,size[0],size[1])
        listBox.grid(row=corrdinate[0],column=corrdinate[1],rowspan=span[0],columnspan=span[1])
        return listBox

    def create_scrollBar(self,window,corrdinate,rowspans=0,columnspans=0):
        print("Created a ScroolBar")
        scrollBar = Scrollbar(window)
        if columnspans==0 and columnspans==0:
            scrollBar.grid(row=corrdinate[0],column=corrdinate[1])
        elif columnspans==0 and rowspans>0:
            scrollBar.grid(row=corrdinate[0],column=corrdinate[1],rowspan=rowspans)
        elif columnspans>0 and rowspans==0:
            scrollBar.grid(row=corrdinate[0],column=corrdinate[1],columnspan=columnspans)
        return scrollBar

    def create_button(self,window,content,widths,corrdinate,command):
        print("Created a Button")
        button = Button(window,text=content,width=widths,command=command)
        button.grid(row=corrdinate[0],column=corrdinate[1])
