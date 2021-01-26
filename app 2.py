

from tkinter import *

import os

'''
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        print(tempApps)
        apps = [x for x in tempApps if x.strip()]

import os, sys, subprocess
'''


root = Tk()
root.title('App Title')
root.geometry("400x600")


#top of screen
e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Name: ")




#.get pulls from the 'mytextbox' entry that is defined below
def hello():
    hello_label = Label(root, text="Hello " + myTextbox.get())
    hello_label.pack()

def myClick():
    myLabel3 = Label(root, text="LOok! I clicked a button")
    myLabel3.pack()

myLabel = Label(root, text = "Enter you first name")

myLabel.pack()



myTextbox = Entry(root, width=30)
myTextbox.pack()

myButton = Button(root, text="Submit", command=hello, fg="green")
myButton.pack()



myLabel1 = Label(root, text = "Label One")

myLabel1.pack()

myButton1 = Button(root, text="Click Me!", command = myClick, fg="blue")
myButton1.pack()






root.mainloop()


