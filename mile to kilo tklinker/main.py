from tkinter import *

window=Tk()
window.title("Miles to Kilometer")
window.minsize(200,50)
window.config(padx=20,pady=20)

temp= Label()
temp.grid(row=0,column=0)

mile_entry=Entry()
mile_entry.grid(row=0,column=1)

mile=Label(text="Miles")
mile.grid(row=0,column=2)

is_equals=Label(text="is equal to")
is_equals.grid(row=1,column=0)

result_km=Label()
result_km.grid(row=1,column=1)

km=Label(text="Km")
km.grid(row=1,column=2)

def calculate():
    m=int(mile_entry.get())
    k=m*1.6
    result_km.config(text=str(k))

calc=Button(text="Calculate", command=calculate)
calc.grid(row=2,column=1)

window.mainloop()
