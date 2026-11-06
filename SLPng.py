# Prequisites
import time
from time import sleep
import os
import platform
import sys
def cc(): # Console clearing function
    oss = platform.system()
    if oss=="Windows":
        os.system("cls")
    elif oss=="Darwin" or oss=="Linux":
        os.system("clear")

n=0 # Floor numbers
def retn(): # Input type checker
    try:
        n = input("How many floors do you want in your building? ") # Floor number input
        if(n=="q"):
            cc()
            print("Thank you for using the lift program, see you later!")
            time.sleep(3)
            n=0
            sys.exit()
        n=int(n)
    except ValueError:
        print("Input must be a floor number, or 'q' to quit the program")
        time.sleep(3)
        retn()
retn()
cc()
cs = [0] # Floor targets. 0 is just a placeholder.
di = "IDLE" # Direction lift is heading
cf = 1 # Current floor
cs.pop() # Remove 0 from the array
running = True
while (running==True):
    cc()
    print(f"There are {n} floors in this building")
    print(f"Current floor: {cf}")
    print(f"Direction: {di}")
    print(f"Next floor target in order :")
    for i in range(len(cs)):
        print(f"- {cs[i]}")
    nf=input("What's your floor target? ('q' to quit the program) ") # Floor target input
    # Explanation of the system
    # The lift will put the desired floor from user (nf) to list of next floors (cs) only
    # if nf is in the same direction as where the lift is heading
    # for example, the nf is 9, while the current floor (cf) is 5 
    # and the direction (di) is ASCENDING. 9 will be added to cs.
    # else, input is discarded, and user will have to input again when the direction is
    # aligned, or the lift is IDLE
    # In addition, of course, 0 < nf <= n, and nf is not already in cs
    
    if(nf!="q"): # Making sure the input type is valid
        try:
            nf=int(nf)
        except ValueError:
            print("Input must be a floor number, or 'q' to quit the program")
            time.sleep(3)
            nf=""

    if(nf=="q"):
        cc()
        print("Thank you for using the lift program, see you later!")
        time.sleep(3)
        break
    elif(nf==""):
        time.sleep(0.0001)
    elif ((di=="IDLE" or (di=="ASCENDING" and int(nf)>cf) or (di=="DESCENDING" and int(nf)<cf)) and (int(nf)>0 and int(nf)<=n) and (int(nf) not in cs)):
        cs.append(int(nf))
    elif(int(nf) in cs):
        print("The floor you entered is already in the list")
        time.sleep(3)
    elif(int(nf)<=0 or int(nf)>n):
        print("The floor number you entered is out of range")
        time.sleep(3)
    else:
        print("The floor number you entered is not on the direction the lift is heading. Please enter again when the lift direction has reversed/when the lift is idle")
        time.sleep(5)
    
    # Movement
    if(di=="ASCENDING"):
        cf+=1
    elif(di=="DESCENDING"):
        cf-=1
    else:
        cf=cf # Just to prevent any errors
    
    # Floor number remover
    if cf in cs:
        cs.remove(cf)

    # Floor status manager
    if not cs:
        di="IDLE" # If no target floor, IDLE
    else: 
        if(di=="IDLE"): # Lift mover from IDLE position
            if(cf>cs[0]):
                di="DESCENDING"
            else:
                di="ASCENDING"
