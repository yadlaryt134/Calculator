
import tkinter as tk
import tkinter.messagebox
from tkinter import *
import math
from collections import Counter

root = tk.Tk()

root.title("Calculator")

e = Entry(root, width=25, borderwidth=1)
e.grid(row=0, column=0,columnspan=4,padx=10,pady=10)

global new
new = True

global expr
expr = []

def storage(x):

    global new
    global expr

    if new:
        clear()
        new = False
    
    expr.append(x)

    # display unicode 
    
    if x == "*":
        x = u"\u00D7"
    elif x == "/":
        x = u"\u00F7"
    elif x == "**":
        x = u"\u005E"

    e.insert(tk.END, x)

def enterKey(event):
    evaluate()

def inputConversion():

    counter = e.get().count("^")

    line = e.get().replace("^", "**", counter)

    return line


def evaluate():

    global new
    global expr

    str_expr = ''.join(expr)

    if expr:

        try:
            line = str_expr

            # for when '^' is typed in the entry, exponents will evaluate
            if "^" in e.get():
                line = inputConversion()

            sum = str(eval(line))
            clear()
            f_sum =  float(sum) 
            f_sum = round(f_sum, 3)
            e.insert(tk.END,f_sum)
        except:
            clear()
            e.insert(tk.END, "Invalid Input")
    else: # in case all of the input was typed in the entry
        try:
            counter = 0
            line = e.get()

             # for when '^' is typed in the entry, exponents will evaluate
            if "^" in e.get():
                line = inputConversion()

            sum = str(eval(line))
            clear()
            f_sum =  float(sum) 
            f_sum = round(f_sum, 3)
            e.insert(tk.END,f_sum)
        except:
            clear()
            e.insert(tk.END, "Invalid Input")

    new = True

def clear():
    global expr

    expr.clear()
    e.delete(0, tk.END)

def backArrow():

    global expr

    length = len(expr)

    e.delete(length-1, length+1)

    try:
        expr.pop()
    except:
        clear()

def qFormula():
    
    clear()
    e.insert(tk.END, "Type a: ")

    
# numbers buttons

oneButton = tk.Button(root, text="1", height=2, width=5, command=lambda: storage('1')).grid(row=1, column=0)

twoButton = tk.Button(root, text="2", height=2, width=5, command=lambda: storage('2')).grid(row=1, column=1)

threeButton = tk.Button(root, text="3", height=2, width=5, command=lambda: storage('3')).grid(row=1, column=2)

fourButton = tk.Button(root, text="4", height=2, width=5, command=lambda: storage('4')).grid(row=2, column=0)

fiveButton = tk.Button(root, text="5", height=2, width=5, command=lambda: storage('5')).grid(row=2, column=1)

sixButton = tk.Button(root, text="6", height=2, width=5, command=lambda: storage('6')).grid(row=2, column=2)

sevenButton = tk.Button(root, text="7", height=2, width=5, command=lambda: storage('7')).grid(row=3, column=0)

eightButton = tk.Button(root, text="8", height=2, width=5, command=lambda: storage('8')).grid(row=3, column=1)

nineButton = tk.Button(root, text="9", height=2, width=5, command=lambda: storage('9')).grid(row=3, column=2)

zeroButton = tk.Button(root, text="0", height=2, width=5, command=lambda: storage('0')).grid(row=4, column=0)


# function buttons

root.bind('<Return>',enterKey)

plusButton = tk.Button(root, text="+", height=2, width=5, command=lambda: storage('+')).grid(row=1, column=3)

minusButton = tk.Button(root, text="-", height=2, width=5, command=lambda: storage('-')).grid(row=2, column=3)

openParen = tk.Button(root, text="(", height=2, width=5, command=lambda: storage('(')).grid(row=4, column=1)

closeParen = tk.Button(root, text=")", height=2, width=5, command=lambda: storage(')')).grid(row=4, column=2)

divButton = tk.Button(root, text=u"\u00F7", height=2, width=5, command=lambda: storage('/')).grid(row=3, column=3) # diviison symbol

multButton = tk.Button(root, text=u"\u00D7", height=2, width=5, command=lambda: storage('*')).grid(row=4, column=3) # multiplication symbol

decimalButton = tk.Button(root, text=".", command=lambda: storage('.'), height=2, width=5).grid(row=5, column=2)

exponentButton = tk.Button(root, text="^", command=lambda: storage('**'), height=2, width=5).grid(row=5, column=3)

equalButton = tk.Button(root, text="=", command=lambda: evaluate(), height=2, width=12).grid(row=6, column=2, columnspan=2)

backButton = tk.Button(root, text=u"\u2190", command=lambda: backArrow(), height=2, width=12).grid(row=5, column=0,columnspan=2) # backspace arrow

clearButton = tk.Button(root, text="Clear", command=lambda: clear(), height=2, width=12).grid(row=6,column=0, columnspan=2)




root.mainloop()