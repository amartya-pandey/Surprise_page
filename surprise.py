import math
import time
from turtle import *


name_ = "Amartya"
crush_name = "Shreya"
def hearta(k):
    return 15*math.sin(k)**3

def heartb(k):
    return 12*math.cos(k)-5*\
        math.cos(2*k)-2*\
        math.cos(3*k)-\
        math.cos(4*k)

def Write_for_madam(bg_col, f_col):
    penup()
    goto(0,0)
    bgcolor(bg_col)
    color(f_col)
    goto(-130, 0)
    write(name_, align="right", font = ("Arial", 15))
    goto(190, 0)
    write(crush_name, align="right", font = ("Arial", 15))

def write_for_madam():
        Write_for_madam("#000000", "#ffffff")
        Write_for_madam("#ffffff", "#000000")
        Write_for_madam("#000000", "#ffffff")

    


def draw_for_madam():
    goto(0,0)
    pendown()
    for i in range(10000):
        goto(hearta(i)*2, heartb(i)*2)
        for j in range(5):
            color("#f73487")
        goto(0,0)
    done()

def ask_madam():
    print("Can I \U0001F97A \n \t\ty | n")
    like = input()

    if(like == "y"):
        write_for_madam()
        draw_for_madam()
    
    else:
        print("\n"*60)
        print("Please \U0001F62D \n please.. please..")
        print("\n"*10)

        ask_madam()

def main():
    print("Hlo..\U0001F601")
    time.sleep(3)

    print("I wanted to say !!! something\U0001F605 !!!")

    time.sleep(3)
    ask_madam()

if __name__ =="__main__": 
    main()