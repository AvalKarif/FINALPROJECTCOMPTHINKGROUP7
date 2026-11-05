import time
from time import sleep
import tkinter as tk
from tkinter import *
wh = 700 # Window
ww = 1900
nw = 50 # Number
nm = 15
fx = 100 # Floor
fw = 400
n = 15 # Floor number
fh=(wh*n)/(n**2 + n -1)
gh=fh/n # I forgot
fy=gh
bx=int(fh*2) # Button size
by=12

w = Tk()
w.geometry(f"{ww}x{wh}")
w.title("Simple Lift Program")
w.configure(bg="black")

c = Canvas(w,width=ww,height=wh)
c.configure(bg="black")
c.pack()

co=0 # Counter for loop to prevent mismatch
cs=[1] # 0 is placeholder
di="IDLE" # Direction of lift
cf=1 # Current floor
pf=cf # Previous floor, used as minus reference

def bp(floor):# Button action
    global di
    if ((di=="IDLE" or (di=="ASCENDING" and int(floor)>cf) or (di=="DESCENDING" and int(floor)<cf)) and (int(floor)>0 and int(floor)<=n) and (int(floor) not in cs)):
        cs.append(int(floor))
        print(di)
        print(cs)
    else:
        time.sleep(0.001) 
    if(di=="IDLE"): # Lift mover from IDLE position
        if(cf>cs[0]):
            di="DESCENDING"
        else:
            di="ASCENDING"

bx = [0 for i in range(n)]
by = [0 for i in range(n)]
gb=ww-(ww-fx-fw)
sbc=0 # Make sure every line is 2 numbers only

fo=Frame(w, height=wh, width=by)
fo.place(x=(gb+5*by), y=5)
fe=Frame(w, height=wh, width=by)
fe.place(x=gb+20*by, y=5)
for j in range(1, (n+1)):
    #by[j-1]=(sbc+1)+int(sbc*(ww/n))/2
    if((j%2)==0):
        bx[j-1]=gb+bx
        sbc+=1
        l = Button(fe, text=j, command=bp(j), width=bx, height=by-7).pack()
    else:
        #bx[j-1]=gb-bs
        l = Button(fo, text=j, command=bp(j), width=bx, height=by-7).pack()

for i in range(1, (n+1)): # Floor creator
    co=i
    fye=fy+fh
    fxe=fx+fw
    i = c.create_rectangle(fx, fy, fw, fy+fh, fill="#fff1bd")
    i = c.create_rectangle(fx+nm, fy+(1/5)*fh, fx+nm*5, fye-(1/5)*fh, fill="white")
    i = c.create_text(fx+45, ((fy+fye)/2), text=co)
    fy+=fh+gh


if(di=="IDLE" and cs): # Lift mover from IDLE position
    if(cf>cs[0]):
        di="DESCENDING"
    else:
        di="ASCENDING"
elif(di=="ASCENDING"):
    cf+=1
elif(di=="DESCENDING"):
    cf-=1

w.mainloop()
