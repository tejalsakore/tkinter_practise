#Entry widget is used to take input
from tkinter import Tk,Label,Button,Entry,mainloop

window = Tk()
window.title("GUI")
window.geometry('500x500')

l1 = Label(window,font=("Arial",30))
l1.grid(column=1,row=5)

txt = Entry(window,width=20)
txt.grid(column=1,row=0)


def clicked():
    res ="Welcom to "+txt.get()
    l1.configure(text=res)                            #will execute on click event

bt = Button(window,text="Enter",bg="yellow",fg="red",command=clicked) #connecting button to the function
bt.grid(column=1,row=6)

mainloop()