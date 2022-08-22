from tkinter import Tk,Label,mainloop

window = Tk()
window.title("GUI") 
i1 =Label(window,text="Heyyyaa!",font=("Arial Bold",50))
i1.grid(column=0,row=0)  #grid()->set thr position of window
mainloop()