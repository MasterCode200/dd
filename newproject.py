from tkinter import *
from tkinter.ttk import*
from time import strftime


def convert24(str1):
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    

    elif str1[-2:] == "AM":
        return str1[:-2]
    
    elif str1[-2:] == "PM" and str1[2:] == "12":
        return str1[-2:]
    
    else:
        return str(int(str1[2:]) + 12) + str1[2:8]


root = Tk()
root.title("Digital Clock")

def clock():
    tick = strftime('%H:%M:%S %p')
    c=convert24(tick)
    #write logic here to convert GMT24------->IST24
    #IST = GMT + 5 hours 30 min
    #slicing --add --h and m
    s1 = c[6:8]
    h1 = str(int(c[0:2])+1)
    m1 = str(int(c[3:5])+30)
    ft = h1+':'+m1+':'+s1
    label.config( text = ft)

    label.after(1000,clock)
label = Label(root,font=('sans',80),background='yellow',foreground='green')

label.pack(anchor="center")

clock()
mainloop()