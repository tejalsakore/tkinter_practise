from tkinter import Tk,mainloop,Label,Checkbutton,BooleanVar

window =Tk()
window.title("GUI")
window.geometry("500x500")

l1 =Label(window,text="Heyyyaa!Are you Indian?",font=("Arial Bold",20))
l1.grid(column=0,row=0)

chk_state1 =BooleanVar() #creating a variable of type BooleanVar which is not a standard Python variable, it's a Tkinter variable
chk_state2 =BooleanVar()
chk_state1.set(False)
chk_state2.set(False)
chk1 = Checkbutton(window,text="Yes",var=chk_state1)
chk2 = Checkbutton(window,text="No",var=chk_state2)
chk1.grid(column=1,row=2)
chk2.grid(column=1,row=3)

mainloop()