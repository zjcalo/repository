from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import sqlite3

import mysql.connector

import csv

import numpy as np
import matplotlib.pyplot as plt

import requests
import json


from tkinter import ttk



root = Tk()
root.title('Entry Boxes')
root.geometry("400x400")

# define this right at the 
# beginning of the program so 
# that it can be overwritten in the click function

myLabel = Label(root)


# this is one way to delete things

'''
def myDelete():
    #myLabel.pack_forget()
    myLabel.grid_forget()
    #myLabel.destroy()
    myButton['state'] = NORMAL
'''


def myClick():
    global myLabel
    
    myLabel.destroy()
    
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, 'end')
    myLabel.grid(row=3, column=0, pady=10)
    
    # this  disables the button at this 
    # point in the sequence so that it 
    # only becomes disabled after the label 
    # gets packed onto the screen

    #myButton['state'] = DISABLED

e = Entry(root, width=17, font=('Helvetica', 24))
e.grid(row=0, column=0, pady=10)

myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.grid(row=1, column=0, pady=10)


'''
deleteButton = Button(root, text="Delete Text", command=myDelete)
deleteButton.grid(row=2, column=0, pady=10)
'''


root.mainloop()