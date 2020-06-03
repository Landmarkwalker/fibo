# Description: fibonacci thing
# Date: 29 / May / 19 BBY
# By: Daniel Mcinerney
from tkinter import *
from tkinter import ttk
import tkinter as tk
#import turtle

home = Tk()
#home = tk.Tk()
home.title('Fibonacci drawing Turtle')
home.geometry("500x400+650+100")

#title
title = Label(home, text="Fibonacci")
title.config(font='Helvetica 25 bold')
title.grid(row=0, column=1)
#labels
lblOutputAnswer = Label(home, text = "hello")
lblOutputAnswer.grid(row = 4, columnspan = 2)
#lblOutputAnswer1 = tk.Text(home, text = "hello")
#lblOutputAnswer1.pack()
#func/

def enter():
    prev = entFib.get()
    fibo = entFib1.get()
    for i in range(int(entTimes.get())):
        prev, fibo = fibo, int(prev) + int(fibo)
        print(fibo)

def Turtle():
    bob = turtle.Turtle()

#button for turtle
butTurtle = ttk.Button(home, text = "Draw!", command = Turtle)
butTurtle.grid(row=0, column=2)

butEnter = ttk.Button(home, text = "Enter!", command = enter)
butEnter.grid(row=2, column= 2)
#numbers
entFib = ttk.Entry(home, width = 20)
entFib.grid(row = 0, column = 3)
entFib1 = ttk.Entry(home, width = 20)
entFib1.grid(row = 2, column = 3)
entTimes = ttk.Entry(home, width = 20)
entTimes.grid(row = 3, column = 3)

home.mainloop()