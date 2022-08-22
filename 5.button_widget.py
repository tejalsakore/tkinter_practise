from tkinter import Tk,mainloop,Label,Button

window = Tk()
window.title("GUI")
l1 = Label(window,text="Press Enter",font=("Arial",20))
window.geometry('500x500')
l1.grid(column=1,row=5)

bt = Button(window,text="Enter",bg="yellow",fg="red")
bt.grid(column=1,row=6)

mainloop()