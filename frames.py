from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename


root = Tk()
root.title('Frames with Tkinter')
root.geometry("900x900")

frame = LabelFrame(root, text = "This is my frame...", padx=5, pady=5)
frame.pack(padx=2, pady=2)

# within frame padding = first line
# outside frame padding = second line


b = Button(frame, text="Don't Click Here")
b.grid(row=0, column=0)

# tkinter variables can either be set or get

#r = IntVar()
#r.set("2")


# The first string is the name, the second is the value



MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")



# loop through the MODES list, the first value is text and the second is the mode, which
# is the second object in the list

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

# not necessary to create a list and for loop, but it does save time


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

# Radiobuttons

#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=pizza.get())
myLabel.pack()

# with frames, you can use GRID positioning and PACK positioning in the same output file

# the frame is packed within the root
# but the button is grid within the frame



c = Button(root, text="Click Here", command=lambda: clicked(pizza.get()))
c.pack()

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

'''

def popup():
    response = messagebox.askyesno("This is my Popup! TITLE", "Hello World, this is the message in the popup")
    #Label(root, text=response).pack()
    # When we click yes, the label text response generates a 1
    # and when we click no, it generates a 2
    # that is where the 1 below came from
    if response == 1:
        Label(root, text="You clicked yes").pack()
    else:
        Label(root, text="You clicked no").pack()
'''
# okcancel also returns a 1 and 0

# askquestion returns a yes or no instead of 1 and 0

# showerror, showwarning, and showinfo returns ok


def popup():
    response = messagebox.askquestion("This is my Popup! TITLE", "Hello World, this is the message in the popup")
    Label(root, text=response).pack()
    if response == "yes":
        Label(root, text="You clicked yes").pack()
    else:
        Label(root, text="You clicked no").pack()



Button(root, text="Popup", command=popup).pack()

#this button makes a popup box show up with the text inside it


# opening new windows

def open():
    top = Toplevel()
    top.title("Second Windw")
    lbl = Label(top, text = "Hello World").pack()
    btn2 = Button(top, text="close window", command = top.destroy).pack()

btn = Button(root, text = "Open Second Window", command=open).pack()


#root.filename = filedialog.askopenfilename(initialdir = "/", title = "Select A File", filetypes = (("all", "*.*")))

# this kind of works but not quite and I don't know why

def openFile():
    global my_file
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("txt", "*.text"), ("all files", "*.*")))
    file_label = Label(root, text=filename).pack()
    my_file = filename
    return filedialog.askopenfilename()
'''

def openFile():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.text"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    #txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")
'''


# this button technically works, but it doesn't actually open the file?

# not sure why so commenting it out to save space

#mybtnfile = Button(root, text = "Open File", command = openFile).pack()



vertical = Scale(root, from_ = 0, to=900)

vertical.pack()


def slide():
    sliderlabel = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x900")


horizontal = Scale(root, from_ = 0, to=900, orient=HORIZONTAL)
horizontal.pack()

sliderlabel = Label(root, text=horizontal.get()).pack()





sliderbtn = Button(root, text="press to print slider number", command=slide).pack()


# an integer variable called 'var'

var = IntVar()

# creating a check box - process involved

# the show function needs to be created so we can see
# the output of clicking on the checkbox

# var.get essentially GETS whatever the variable IntVar actually is

def show():
    varLabel = Label(root, text=var.get()).pack()


# this is creating a check box

c = Checkbutton(root, text = "Check this box", variable = var )
c.pack()


# this is creating a button so that we have a way to run the command
# show that we created above, which is needed to output the checkbox



varButton = Button(root, text="Show Selection", command = show).pack()


# checking the box = 1, unchecked = 0


# creating a string variable

# and adding a 2 to the end of the variable, the function
# the checkbox value and the button name

# in this one, I added the on and off values to the actual checkbutton
# so that when it is either checked or unchecked, the button will output
# specific values


var2 = StringVar()

def show2():
    varLabel = Label(root, text=var2.get()).pack()

# deselect has to be added to make it run correctly

c2 = Checkbutton(root, text = "Check this box STRING", variable = var2, onvalue="on", offvalue="off")
c2.deselect
c2.pack()

var2Button = Button(root, text="Show Selection", command = show2).pack()


# drop down menus

# assign root or frame etc, then the variable, then the values
# within the variable
# below is text so we assigned the variable as a string var

clicked = StringVar()

# this sets a default from the listed strings below

clicked.set("Monday")


drop = OptionMenu(root, clicked, "monday", "tuesday")
drop.pack()


def dropshow():
    dropLabel = Label(root, text=clicked.get()).pack()



dropButton = Button(root, text="Show Selection from Drop", command = dropshow)
dropButton.pack()



# creating a more complicated drop down with lists


options = [
    "Saturday",
    "Sunday",
    "Every Day",
    "Snow Day"
]

clicked2 = StringVar()

# the 0 refers to the index value

clicked2.set(options[0])

# need to add a star before the list name, in this case options

drop2 = OptionMenu(root, clicked2, *options)
drop2.pack()

# I accidentally set the text below to clicked instead of clicked2

# when I did that, it updated BOTH drop down menus which was interesting

# if you need to update variables in multiple places

def dropshow2():
    dropLabel2 = Label(root, text=clicked2.get()).pack()



dropButton2 = Button(root, text="Show Selection from Drop", command = dropshow2)
dropButton2.pack()




mainloop()