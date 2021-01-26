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



class Elder:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(master, text = "Click Me!", command=self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("Look at you... you clicked a button!")



e = Elder(root)





root.mainloop()