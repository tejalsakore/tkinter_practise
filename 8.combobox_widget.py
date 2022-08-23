# Combobox gives dropdown menu
from tkinter import Tk,Label,mainloop,ttk #ttk is imported on behalf of combobox

window = Tk()
window.title("GUI")
window.geometry('500x500')

l1 =Label(window,text="Select Your Language",font=("Arial Bold",20))
l1.grid(column=0,row=0)

combo = ttk.Combobox(window)
combo["values"]=("Select","Marathi","Hindi","English","Other") #adding combobox items using the tuple
combo.current(0) #Setting selected item
combo.grid(column=2,row=0)

mainloop()


