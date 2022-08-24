from tkinter import Tk,mainloop,INSERT
from tkinter.scrolledtext import ScrolledText

window = Tk()
window.title("ScrolledText Widget")
window.geometry('500x500')

st =ScrolledText(window,width=50,height=10)
st.insert(INSERT,"this is srcollbar")
st.grid(column=0,row=0)

mainloop()

