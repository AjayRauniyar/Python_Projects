# lets import some module
from tkinter import *
from tkinter.ttk import *

# some important function to retrieve system time :)
from time import strftime

#creating tkinter window 
root = Tk()
root.title('clock')
 
#let's display time on the label yaa
def time():
    string =strftime('%H :%M :%S %p')
    label.config(text =string)
    label.after(1000,time)

#lets give some fantastic look to clock 
label= Label(root,font = ('DS-Digital',40,'bold'),background='black',foreground='blue')

#Now lets place the  clock :)
label.pack(anchor ='s')
time()


mainloop()