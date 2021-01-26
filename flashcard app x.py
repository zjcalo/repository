from tkinter import *
from tkinter import ttk
import PIL
from PIL import Image
from PIL import ImageTk
from random import randint

root = Tk()
root.title('Flashcard')
root.geometry("1600x900")


# Create randomizing function




# Create currency answer question

def currency_answer():
    answer = answer_input.get()
    
    # replaces a space with no space
    
    answer = answer.replace(" ", "")

    # determine right or wrong and convert to lower case

    if answer.lower() == our_currency[rando]:
        response = "Correct!"
    else:
        response = "incorrect"

    # generates the typed response in lower case

    answer_label.config(text=response)


# Create state flashcard function


def states():
    # Hide previous frames
    hide_all_frames()
    state_frame.pack(fill=BOTH, expand=1)
    my_label = Label(state_frame, text="States").pack()


    

    # Create a list of currency
    global our_currency
    our_currency = ['twenty', 'ten', 'one', 'hundredk', 'fivehundred']

    # Generate a random number based on length of the our currency list
    # and -1 to account for the 0 index position of the first item
    
    global rando
    rando = randint(0, len(our_currency)-1)

    # passes in a random number to associate with a list index

    currency = "currency/" + our_currency[rando] + ".png"
    # Create currency images
    
    global currency_image
    #currency_image = ImageTk.PhotoImage(Image.open('currency/twenty.jpg'))
    currency_image = PhotoImage(file = currency)
    
    
    

    # passes in a random number to associate with a list index

   
    
    
    # Create currency images

    
    show_currency = Label(state_frame, image = currency_image).pack()
    

    # create button to randomize images

    rando_button = Button(state_frame, text="PASS", command=states)
    rando_button.pack()
    
    global answer_input
    answer_input = Entry(state_frame, font=("Helvetica", 18))
    answer_input.pack(pady=15)


    # Create button to answer

    answer_button = Button(state_frame, text="Answer", command=currency_answer)
    answer_button.pack(pady=5)

    # Create a label to tell us if we got the answer right


    global answer_label
    answer_label = Label(state_frame, font=("Helvetica", 18))
    answer_label.pack(pady=15)


# Create state capital flashcard function

def state_capitals():
    # Hide previous frames
    hide_all_frames()
    state_capitals_frame.pack(fill=BOTH, expand=1)
    my_label = Label(state_capitals_frame, text="Capitals").pack()



# Hide all previous frames

def hide_all_frames():
    for widget in state_frame.winfo_children():
        widget.destroy()
    for widget in state_capitals_frame.winfo_children():
        widget.destroy()
    state_frame.pack_forget()
    state_capitals_frame.pack_forget()

# Create menu


my_menu = Menu(root)
root.config(menu=my_menu)

# Create Geo menu items

states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=states_menu)
states_menu.add_command(label = "States", command=states)
states_menu.add_command(label = "State Capitals", command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit", command=root.quit)




# Create our frames



state_frame = Frame(root, width=500, height=500)
state_capitals_frame = Frame(root, width=500, height=500)




root.mainloop()


