#Calling functions whenever an event occurs refers to a binding function.

from curses import window
from tkinter import Tk,mainloop,Label,Button

window =Tk()
window.title("Binding Function")
window.geometry("500x500")

def say_hi():
    Label(window,text="Hiii!").pack()

Button(window, text="Click Me😊",command=say_hi).pack()
mainloop()