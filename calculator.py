from tkinter import *
from math import *

root=Tk()
root.title("Calculator")
root.resizable(0,0)

entry_1=Entry(root,fg='#29DBF9',width=22,highlightcolor='Green',bd=3,bg='#52534C',font=('Courier',15))
entry_1.pack(ipady=5)

topframe=Frame(root,bd=2,relief=RAISED,bg='#29DBF9',colormap='new')
topframe.pack()
bottomframe=Frame(root,bg='#29DBF9',bd=2)
bottomframe.pack(side=BOTTOM)


def button_1():
    entry_1.insert(10,1)
    entry_1.get()
def button_2():
    entry_1.insert(10,2)
    entry_1.get()
def button_3():
    entry_1.insert(10,3)
    entry_1.get()
def button_4():
    entry_1.insert(10,4)
    entry_1.get()
def button_5():
    entry_1.insert(10,5)
    entry_1.get()
    
def button_6():
    entry_1.insert(10,6)
    entry_1.get()
    
def button_7():
    entry_1.insert(10,7)
    entry_1.get()
    
def button_8():
    entry_1.insert(10,8)
    entry_1.get()
    
def button_9():
    entry_1.insert(10,9)
    entry_1.get()
    
def button_add():
    entry_1.insert(10,'+')
    entry_1.get()
def button_sub():
    entry_1.insert(10,'-')
    entry_1.get()
def button_div():
    entry_1.insert(10,'/')
    entry_1.get()
def button_mul():
    entry_1.insert(10,'*')
    entry_1.get()
def button_zero():
    entry_1.insert(10,0)
    entry_1.get()
def button_del():
    entry_1.insert(10,'.')
    entry_1.get()

def evaluate(event):
    a=str(eval(entry_1.get()))
    entry_1.delete(0,END)
    entry_1.insert(10,a)
def entry_1_cls():
    entry_1.delete(0,END)

def entry_1_bs():
    a=str(entry_1.get())
    a=a[:-1]
    entry_1.delete(0,END)
    entry_1.insert(10,a)
    

button_a=Button(topframe,text='1',fg='Blue',command=button_1,height=4,width=8,bd=3)
button_b=Button(topframe,text='2',fg='Blue',command=button_2,height=4,width=8,bd=3)
button_c=Button(topframe,text='3',fg='Blue',command=button_3,height=4,width=8,bd=3)
button_d=Button(topframe,text='4',fg='Blue',command=button_4,height=4,width=8,bd=3)
button_e=Button(topframe,text='5',fg='Blue',command=button_5,height=4,width=8,bd=3)
button_f=Button(topframe,text='6',fg='Blue',command=button_6,height=4,width=8,bd=3)
button_g=Button(topframe,text='7',fg='Blue',command=button_7,height=4,width=8,bd=3)
button_h=Button(topframe,text='8',fg='Blue',command=button_8,height=4,width=8,bd=3)
button_i=Button(topframe,text='9',fg='Blue',command=button_9,height=4,width=8,bd=3)

button_10=Button(topframe,text= '+',fg='Blue',command=button_add,height=4,width=8,bd=3)
button_11=Button(topframe,text= '-',fg='Blue',command=button_sub,height=4,width=8,bd=3)
button_12=Button(topframe,text= '/',fg='Blue',command=button_div,height=4,width=8,bd=3)
button_13=Button(topframe,text= '*',fg='Blue',command=button_mul,height=4,width=8,bd=3)

button_14=Button(topframe,text='0',fg='Blue',command=button_zero,height=4,width=8,bd=3)
button_15=Button(topframe,text='.',fg='Blue',command=button_del,height=4,width=8,bd=3)
button_16=Button(topframe,text='=',fg='Blue',height=4,width=8,bd=3)
button_17=Button(bottomframe,text='Clear',fg='blue',command=entry_1_cls,height=4,width=18,bd=3)
button_18=Button(bottomframe,text='Back Space',fg='blue',command=entry_1_bs,height=4,width=18,bd=3,highlightcolor='red')

button_a.grid(row=1)
button_b.grid(row=1,column=1)
button_c.grid(row=1,column=2)
button_d.grid(row=2)
button_e.grid(row=2,column=1)
button_f.grid(row=2,column=2)
button_g.grid(row=3)
button_h.grid(row=3,column=1)
button_i.grid(row=3,column=2)

button_10.grid(row=1,column=3)
button_11.grid(row=2,column=3)
button_12.grid(row=3,column=3)
button_13.grid(row=4,column=3)

button_14.grid(row=4)
button_15.grid(row=4,column=1)
button_16.grid(row=4,column=2)
button_17.grid(row=5)
button_18.grid(row=5,column=1)

entry_1.bind("<Return>", evaluate)
button_16.bind("<Button-1>", evaluate)


