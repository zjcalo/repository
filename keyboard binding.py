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
root.title('Classes')
root.geometry("400x400")

# this gives positional data on where the button was clicked
'''
def clicker(event):
    myLabel = Label(root, text="You clciked a button" +str(event.x) + " " + str(event.y))
    myLabel.pack()
'''


def clicker(event):
    myLabel = Label(root, text="You clciked a button")
    myLabel.pack()

myButton = Button(root, text="Click Me", command=clicker)


# Button-1 = regular click
# Enter and Leave is whether the mouse hovers over the Button widgets

myButton.bind("<Button-1>", clicker)
#myButton.bind(event, action)
myButton.pack(pady=20)



root.mainloop()