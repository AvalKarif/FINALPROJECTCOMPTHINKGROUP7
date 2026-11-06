# Prequisites
import time
from time import sleep
import tkinter as tk
from tkinter import *
# Scaler window setup
scale=Tk()
scale.title("Pick your floor number")
scale.geometry("400x100")
inp=DoubleVar()
Label(scale, font=("Arial", 14, "bold"),fg="darkblue",text="Pick the number of floors in the building").pack()
s=Scale(scale, from_=1,to=50,variable=inp,orient=HORIZONTAL)
s.pack()

def launch():
    scale.withdraw()
    global w
    n=int(inp.get())
    wh = 1080 # Window
    ww = 1920
    nx = 50 # Number
    fx = 300 # Floor
    fw = 400
    fh=int((wh-370)/n)
    fy=wh-355
    
    bx=20 # Button
    by=7

    w = Toplevel() # Child window properties
    w.geometry(f"{ww}x{wh}")
    w.title("Simple Lift Program")
    w.configure(bg="black")

    c = Canvas(w,width=fw,height=wh-355) # Canvas for the building with elevator
    c.configure(bg="grey")
    c.place(x=0, y=0)

    co=0 # Counter for loop to prevent mismatch
    cs=[1] # 0 is placeholder
    cs.pop()
    di="IDLE" # Direction of lift
    cf=1 # Current floor
    pf=cf # Previous floor, used as minus reference
    def bp(floor):# Button action
        nonlocal di
        if ((di=="IDLE" or (di=="ASCENDING" and int(floor)>cf) or (di=="DESCENDING" and int(floor)<cf)) and (int(floor)>0 and int(floor)<=n) and (int(floor) not in cs)):
            cs.append(int(floor))
        else:
            time.sleep(0.001) 
        if(di=="IDLE"): # Lift mover from IDLE position
            if(cf>cs[0]):
                di="DESCENDING"
            else:
                di="ASCENDING"

    gb=ww-(ww-fx-fw)
    sbc=0 # Make sure every line is 2 numbers only

    fo=Frame(w, height=wh, width=bx) # Frame for odd numbers
    fe=Frame(w, height=wh, width=bx) # Frame for even numbers

    fe.place(x=(gb+200), rely=.5, anchor="center") # Frame Placers
    if(n%2==0):
        fo.place(x=gb, rely=.5, anchor="c")
    else:
        fo.place(x=gb, rely=.5, anchor="c")

    for j in range(1, (n+1)): # Button Placers
        if((j%2)==0):
            sbc+=1
            button = Button(fe, text=j, command=lambda f=j:bp(f), width=bx, height=by-7)
        else:
            button = Button(fo, text=j, command=lambda f=j:bp(f), width=bx, height=by-7)
        button.pack()
    co=1
    mar=100

    for i in range(1, (n+1)): # Floor creator
        fye=fy-fh
        c.create_rectangle(mar+nx, fy, fx, fye, fill="#fff1bd")
        c.create_rectangle(mar, fy, mar+nx, fye, fill="white")
        c.create_text(mar+int(nx/2), ((fy+fye)/2), text=co)
        fy-=fh
        co+=1
    lc = (mar+nx+fx)/2
    li = c.create_rectangle(lc-20, wh-355-fh, lc+20, wh-355, fill="blue")
    
    def qc(): # Floor number change
        global n
        scale.deiconify()
        n=DoubleVar()
        w.destroy()
    exif = Button(w, text="Change Floor Number", command=qc)
    exif.pack()

    def check(): # Movement checker
        nonlocal cs
        nonlocal cf
        nonlocal di
        if cf in cs:
            cs.remove(cf) 
            time.sleep(1)
        if not cs:
            di="IDLE"
            texte=""
        if(di=="ASCENDING"):
            cf+=1
            c.move(li, 0, -fh)
        elif(di=="DESCENDING"):
            cf-=1
            c.move(li, 0, fh)
        w.after(100, check)
    w.after(100, check)

Button(scale, text="Launch Program", command=launch).pack()
scale.mainloop()
