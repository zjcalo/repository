from tkinter import *
from tkinter import ttk
import PIL
from PIL import Image
from PIL import ImageTk
from random import randint
from random import randint
import random

root = Tk()
root.title('Flashcard')
root.geometry("1600x900")



def currency_pair_answer():
    if currency_radio.get() == our_currency_pairs[answer]:
        response = "Correct"
    else:
        response = "Incorrect"
    
    answer_currency_pair_label.config(text=response)

    





# Create randomizing function




def random_currency():

    

    # Create a list of currency
    global our_currency
    our_currency = ['twenty', 'ten', 'one', 'hundredk', 'fivehundred']

    # Generate a random number based on length of the our currency list
    # and -1 to account for the 0 index position of the first item
    
    global rando
    rando = randint(0, len(our_currency)-1)

    # passes in a random number to associate with a list index

    currency = "currency/" + our_currency[rando] + ".png"

    global currency_image
    #currency_image = ImageTk.PhotoImage(Image.open('currency/twenty.jpg'))
    currency_image = PhotoImage(file = currency)
    show_currency.config(image=currency_image)
    #show_currency = Label(state_frame, image=currency_image)
    #show_currency.pack()
    
    
    # This is also one way to do it
    '''
    show_currency = Label(state_frame, image=currency_image)
    show_currency.pack()
    '''

# Create currency answer question

def currency_answer():
    answer = answer_input.get()
    
    # replaces a space with no space
    
    answer = answer.replace(" ", "")

    # determine right or wrong and convert to lower case

    if answer.lower() == our_currency[rando]:
        response = "Correct!" + " " + our_currency[rando].title()
    else:
        response = "incorrect" + " " + our_currency[rando].title()

    # generates the typed response in lower case

    answer_label.config(text=response)

    # Clear existing entry box
    
    # this calls the random currency function after
    # the response to the question has been issued
    
    answer_input.delete(0, 'end')


    random_currency()


# Create state flashcard function


def states():
    # Hide previous frames
    hide_all_frames()
    state_frame.pack(fill=BOTH, expand=1)
    my_label = Label(state_frame, text="States").pack()

    

    
    '''
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
    '''
    
    
    global show_currency
    show_currency = Label(state_frame)
    show_currency.pack()

    random_currency()

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
    global show_currency
    show_currency = Label(state_capitals_frame)
    show_currency.pack(pady=15)


    # Create empty answer list
    answer_list = []

    our_currency = ['twenty', 'ten', 'one', 'hundredk', 'fivehundred']

    global our_currency_pairs
    our_currency_pairs = {
    'twenty':'Jackson', 
    'ten':'Hamilton', 
    'one':'Washington', 
    'hundredk':'Wilson', 
    'fivehundred':'McKinley'
    }

    # Create a random integer that is one less
    # than the length of our list

    global rando
    rando = randint(0, len(our_currency)-1)

    global answer
    # choose a random index value from our list

    answer = our_currency[rando]

    # Generate three random answers, one being the right answer
    count = 1
    
    while count < 4:
        rando = randint(0, len(our_currency)-1)
        
        # if first selection, this is our answer
        
        if count == 1:
            answer = our_currency[rando]
            global currency_image
            currency = "currency/" + our_currency[rando] + ".png"
            currency_image = PhotoImage(file = currency)
            show_currency.config(image=currency_image)

        # add the selection to our answer list    
        answer_list.append(our_currency[rando])

        # remove answer from original list
        our_currency.remove(our_currency[rando])

        # then shuffle the list
        random.shuffle(our_currency)

        # add one to the count
        count +=1

    random.shuffle(answer_list)


    global currency_radio
    currency_radio = StringVar()
    currency_radio.set(our_currency_pairs[answer_list[0]])

    currency_radio_btn1 = Radiobutton(state_capitals_frame, text=our_currency_pairs[answer_list[0]], variable=currency_radio, value=our_currency_pairs[answer_list[0]]).pack()
    currency_radio_btn2 = Radiobutton(state_capitals_frame, text=our_currency_pairs[answer_list[1]], variable=currency_radio, value=our_currency_pairs[answer_list[1]]).pack()
    currency_radio_btn3 = Radiobutton(state_capitals_frame, text=our_currency_pairs[answer_list[2]], variable=currency_radio, value=our_currency_pairs[answer_list[2]]).pack()

    # Pass Button

    pass_button = Button(state_capitals_frame, text="Pass", command=state_capitals)
    pass_button.pack(pady=15)

    # Answer

    answer_button = Button(state_capitals_frame, text="Answer", command = currency_pair_answer)
    answer_button.pack(pady=15)


    # Answer label

    global answer_currency_pair_label
    answer_currency_pair_label = Label(state_capitals_frame, text="")
    answer_currency_pair_label.pack(pady=15)




    print(answer_list)
    print(answer)








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


home_label = Label(root, text="Please use the menu to select").pack()

root.mainloop()


