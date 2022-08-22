#we can set the default wndow size using geometry function

from tkinter import Tk,Label

window = Tk()
window.title("GUI")
i1= Label(window,text="Hey There!",font=("Arial Bold ",60))
window.geometry('500x500')
i1.grid(column=0,row=0)
window.mainloop()
