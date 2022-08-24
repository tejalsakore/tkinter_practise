from tkinter import Button, Tk,mainloop,messagebox

window = Tk()
window.title("Messagebox Widget")
window.geometry("500x500")
def clicked():
    messagebox.showinfo("Message Box","This is message box")

btn = Button(window,text="Enter",command=clicked())

mainloop()
