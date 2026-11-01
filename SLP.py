import time
from time import sleep
import tkinter as tk
from tkinter import *
wh = 500
ww = 800
nw = 50
fw = 100
fw = 10
fh = 20
n = 3

w = Tk()
w.geometry(f"{ww}x{wh}")
w.title("Simple Lift Program")

c = Canvas(w,width=ww,height=wh)
c.pack()

co
for i in range(n):
    co=i
    i = c.create_rectangle(10, 10+(nw+10)*i, nw, nw+(nw+10)*i, fill="white", tags=i)
    #i = c.create_text(10+

w.mainloop()
