from tkinter import *

from tkinter import ttk



root = Tk()
root.title('Menu')
root.geometry("400x400")

def file_new():
    hide_all_frames()
    file_new_frame.pack(fill="both", expand=1)
    myLabel = Label(file_new_frame, text = "You clicked").pack()


def edit_cut():
    hide_all_frames()
    edit_cut_frame.pack(fill="both", expand=1)
    myLabel = Label(edit_cut_frame, text = "You clicked").pack()
    dummyButton = Button(edit_cut_frame, text="FAKE").pack(pady=10)
    child_label = Label(edit_cut_frame, text=edit_cut_frame.winfo_children())
    child_label.pack(pady=10)

    print(edit_cut_frame.winfo_children())


def our_command():
    myLabel = Label(root, text = "You clicked").pack()


# Hide all frames OR destroy all widgets in each frame

def hide_all_frames():
    for widget in file_new_frame.winfo_children():
        widget.destroy()
    for widget in edit_cut_frame.winfo_children():
        widget.destroy()
    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()

# Define a menu

my_menu = Menu(root)
root.config(menu=my_menu)

# Create a menu item

file_menu = Menu(my_menu)
my_menu.add_cascade(label = "File", menu=file_menu)
file_menu.add_command(label = "New...", command = file_new)
# Adds a separator bar in the drop down menu
file_menu.add_separator()
file_menu.add_command(label = "Exit...", command = root.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label = "Edit", menu=edit_menu)
edit_menu.add_command(label = "Cut", command = edit_cut)
edit_menu.add_command(label = "Copy", command = our_command)



file_new_frame = Frame(root, width=400, height=400, bg="red")
edit_cut_frame = Frame(root, width=400, height=400, bg="blue")



root.mainloop()