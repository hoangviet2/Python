from tkinter import *
from UILib import UILibary
from command import commands
uilibary = UILibary()
command = commands
window = Tk()
window.wm_title("Book store")

title_lb = uilibary.create_label(window=window,content="Title",corrdinate=[0,0])
title_Entry = uilibary.create_entry(window=window,corrdinate=[0,1])
year_lb = uilibary.create_label(window=window,content="Year",corrdinate=[1,0])
year_Entry = uilibary.create_entry(window=window,corrdinate=[1,1])
author_lb = uilibary.create_label(window=window,content="Author",corrdinate=[0,2])
author_Entry = uilibary.create_entry(window=window,corrdinate=[0,3])
ISBN_lb = uilibary.create_label(window=window,content="ISBN",corrdinate=[1,2])
ISBN_Entry = uilibary.create_entry(window=window,corrdinate=[1,3])
scrollBar = uilibary.create_scrollBar(window,[2,2],6)
listbox = uilibary.create_boxList([2,0],[6,35],window,[6,2])
listbox.bind('<<ListboxSelect>>',commands.get_select_row(event,listbox,[title_Entry,author_Entry,year_Entry,ISBN_Entry]))
button_ViewAll = uilibary.create_button(window,"View all",20,[2,3],commands.view_All_comd(listbox))
button_SearchEntry = uilibary.create_button(window,"Search Entry",20,[3,3],commands.search_comd(listbox))
button_AddEntry = uilibary.create_button(window,"Add Entry",20,[4,3],commands.add_comd(listbox))
button_Update = uilibary.create_button(window,"Update",20,[5,3],commands.update_comd(listbox))
button_Delete = uilibary.create_button(window,"Delete",20,[6,3],commands.delete_comd(listbox))
button_Close = uilibary.create_button(window,"Close",20,[7,3],command= window.destroy)

window.mainloop()
