from tkinter import Tk,mainloop,Label,Button

window = Tk()
window.title("GUI")
l1 = Label(window,text="Press Enter",font=("Arial",20))
window.geometry('500x500')
l1.grid(column=0,row=5)

bt = Button(window,text="Enter")
bt.grid(column=5,row=5)
mainloop()