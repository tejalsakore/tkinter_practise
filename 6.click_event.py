from tkinter import Tk,mainloop,Button

window = Tk()
window.title("GUI")
window.geometry('500x500')

def clicked():
    l1.configure(text="Button was clicked!")                            # will execute on click event

bt = Button(window,text="Enter",bg="yellow",fg="red",command=clicked()) #connecting button to the function
bt.grid(column=1,row=6)

mainloop()