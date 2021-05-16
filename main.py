import sys
from tkinter import *
import time


def timing():
   
    current_time = time.strftime("%H : %M : %S")
    
    clock.config(text=current_time)
   
    clock.after(200,timing)
 

root=Tk()

root.geometry("600x300")

clock=Label(root,font=("trebuchet",50,"bold"),bg="#577BAD")
clock.grid(row=2,column=2,pady=25,padx=100)
timing()
 

digital=Label(root,text="PyDigiClock",font="ubuntu 24")
digital.grid(row=0,column=2)
 
nota=Label(root,text="Hours        Minutes        Seconds",font="ubuntu 15 bold")
nota.grid(row=3,column=2)
 
root.mainloop()
