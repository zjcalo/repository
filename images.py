from tkinter import *

import Image





root = Tk()

root.title('How to create Icons and Images')

# the icon is in the same directory as the images.py file so
# the rest of the path does not need to be specified 

root.iconbitmap('noun_Skull_715268 resized.ico')
#insert the location in the parens


my_img = ImageTk.PhotoImage(Image.open("noun_Skull_715268.png"))
my_img.pack()








button_quit = Button(root, text="Exit Program", command = root.quit)
button_quit.pack()









root.mainloop()