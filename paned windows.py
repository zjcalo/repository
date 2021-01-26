from tkinter import *

from tkinter import ttk



root = Tk()
root.title('Paned Menu')
root.geometry("400x400")



# Panels

panel_1 = PanedWindow(bd=4, relief="raised", bg="red")
panel_1.pack(fill=BOTH, expand=1)

left_label = Label(panel_1, text="Left Panel")
panel_1.add(left_label)

# Create a second panel

panel_2 = PanedWindow(panel_1, orient = VERTICAL, bd=4, relief="raised", bg="blue")
panel_1.add(panel_2)

top_label = Label(panel_2, text = "Top Label")
panel_2.add(top_label)

bottom_label = Label(panel_2, text = "Bottom Label")
panel_2.add(bottom_label)





root.mainloop()