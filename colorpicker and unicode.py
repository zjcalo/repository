from tkinter import *

from tkinter import ttk

from tkinter import colorchooser



root = Tk()
root.title('Color Picker')
root.geometry("400x400")

# Hex color code is the second item in the python list generated

def color():
    my_color = colorchooser.askcolor()[1]
    myLabel = Label(root, text=my_color).pack(pady=10)
    myLabel = Label(root, text="You picked a color", font=("Helvetica", 32), bg=my_color).pack()
    



myButton = Button(root, text="X", command=color)
myButton.pack()



#UNICODE EX

# Look up unicode codes

# U+00A9 = +u'\u00a9',

mylabel1 = Label(root, text ='41' + u'\u00a9', font=("Helvetica", 32)).pack(pady=10)



root.mainloop()