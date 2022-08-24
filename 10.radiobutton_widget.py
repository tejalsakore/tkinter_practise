from tkinter import Tk,mainloop,Label,Radiobutton

window =Tk()
window.title("GUI")
window.geometry("500x500")

l1 =Label(window,text="Choose your gender:",font=("Arial Bold",20))
l1.grid(column=0,row=0)

rad1 =Radiobutton(window,text="Male",value=1) 
rad2 =Radiobutton(window,text="Female",value=2)
rad3 =Radiobutton(window,text="Other",value=3)

rad1.grid(column=1,row=2)
rad2.grid(column=1,row=3)
rad3.grid(column=1,row=4)

mainloop()