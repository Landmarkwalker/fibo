# Description: fibonacci thing
# Date: 29 / May / 19 BBY
# By: Daniel Mcinerney
from tkinter import ttk
import tkinter as tk
import turtle

home = tk.Tk()
home.title('Fibonacci drawing Turtle')
home.geometry("600x400+650+100")

#title
title = tk.Label(home, text="Fibonacci")
title.config(font='Helvetica 25 bold')
title.grid(row=0, column=1)

#labels
lblOutputAnswer = tk.Label(home, text = "hello")
lblOutputAnswer.grid(row = 4, columnspan = 2)

#Text Box - Output
txtOutput = tk.Text(home, height=10)
txtOutput.grid(row=6, column=0, columnspan=4)
scrollOutput = ttk.Scrollbar(home, orient=tk.VERTICAL, command=txtOutput.yview)
scrollOutput.grid(row=6, column=4, sticky=tk.N+tk.S)
txtOutput.config(yscrollcommand=scrollOutput.set)

def enter():
    prev = entFib.get()
    fibo = entFib1.get()
    for i in range(int(entTimes.get())):
        prev, fibo = fibo, int(prev) + int(fibo)
        txtOutput.insert(tk.INSERT, str(fibo) + '\n')

def Turtle():
    bob = turtle.Turtle()
    prev = int(entFib.get())
    fibo = int(entFib1.get())
    for i in range(int(entTimes.get())):
        prev, fibo = fibo, prev + fibo
        bob.fd(prev)
        bob.lt(90)

#button for turtle
butTurtle = ttk.Button(home, text = "Draw!", command = Turtle)
butTurtle.grid(row=0, column=2)

butEnter = ttk.Button(home, text="Enter!", command=enter)
butEnter.grid(row=2, column=2)
#numbers
entFib = ttk.Entry(home, width=20)
entFib.grid(row=0, column=3)
entFib1 = ttk.Entry(home, width=20)
entFib1.grid(row=2, column=3)
entTimes = ttk.Entry(home, width=20)
entTimes.grid(row=3, column=3)

home.mainloop()
