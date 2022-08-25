from curses import window
from tkinter import Tk,mainloop
import tkinter as ttk

window=Tk()
window.title("Spinbox Widget")
window.geometry("500x500")

spin = ttk.Spinbox(window,from_=0,to=100,width=10)
spin.grid(column=0, row=0)
mainloop()