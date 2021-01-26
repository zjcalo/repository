from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Dropdown Bind')
root.geometry("400x400")



options = [
    "MOnday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]
clicked = StringVar()
# default menu item based on list position
clicked.set(options[0])

def selected(event):
    #myLabel = Label(root, text=clicked.get()).pack()
    if clicked.get() == "Friday":
        myLabel = Label(root, text="Yay! It's Friday!").pack()
    else:
        myLabel = Label(root, text=clicked.get()).pack()




def comboclick(event):

    myLabel = Label(root, text=myCombo.get()).pack()

drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack(pady=20)


myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
myCombo.pack()

#myButton = Button(root, text="Select from List", command=selected)
#myButton.pack()

root.mainloop()