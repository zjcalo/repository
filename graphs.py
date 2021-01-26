from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import sqlite3

import numpy as np
import matplotlib.pyplot as plt

import requests
import json



root = Tk()
root.title('Graph App')
root.geometry("500x500")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()

graphButton = Button(root, text="Graph It!", command=graph)
graphButton.pack()








root.mainloop()