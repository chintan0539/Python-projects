from tkinter import *

window=Tk()
window.title("first GUI program")
window.minsize(400,500)

l1=Label(text="hey this is a label",font=('ariel',15,'bold'))
l1.pack()
def clicked():
    l1["text"]=input.get()


b1=Button(text="click me", command=clicked)
b1.pack()

input= Entry(width=20)
input.pack()


window.mainloop()




