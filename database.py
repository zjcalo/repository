from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import sqlite3
sqlite3.paramstyle = 'named'

root = Tk()
root.title('Databases')
root.geometry("400x400")

# Databases

# Create a database or connect to one

# if the address_book.db doesn't exist, this will create it

# IN THE FUTURE

# the name of the .db file for the databases should be the same

# as the name of the table created below?

conn = sqlite3.connect('address_book.db')

# a cursor is what sends to retrieve / do tasks

cursor = conn.cursor()

# database is a table of columns and rows
# designate what they are
# create table


# text, integers, real (decimal), null, blob

'''
cursor.execute("""CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
            )""")

'''


# after we run the program, it creates the .db file in the directory
# that we are in, for ex pyappdir
# we only need to create it once and then we can comment it out



# create text / entry boxes

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zip = Entry(root, width=30)
zip.grid(row=5, column=1, padx=20)

deletebox = Entry(root, width=30)
deletebox.grid(row=10, column=1)

# create text box labels

fnameLabel = Label(root, text="First Name")
fnameLabel.grid(row=0, column=0, pady=(10,0))

lnameLabel = Label(root, text="Last Name")
lnameLabel.grid(row=1, column=0)

addressLabel = Label(root, text="Address")
addressLabel.grid(row=2, column=0)

cityLabel = Label(root, text="City")
cityLabel.grid(row=3, column=0)

stateLabel = Label(root, text="State")
stateLabel.grid(row=4, column=0)

zipLabel = Label(root, text="Zip")
zipLabel.grid(row=5, column=0)

deleteLabel = Label(root, text="Select ID")
deleteLabel.grid(row=10, column=0)




# Create a submit button and function

# the connection and cursor need to be within the function

# the commit and close also need to be within the function

def submit():
    conn = sqlite3.connect('address_book.db')
    cursor = conn.cursor()
    
    # Insert into table / database

    # Create a dictionary

    cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zip)",
                {
                    'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'address': address.get(),
                    'city': city.get(),
                    'state': state.get(),
                    'zip': zip.get()
                })


    conn.commit()
    conn.close()

    # Clear the textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zip.delete(0, END)


submitButton = Button(root, text="Add Record to Database", command = submit)
submitButton.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# Create a query button and function

# oid = original id which is a key that is created in the database

# print puts it in the terminal

def query():
    conn = sqlite3.connect('address_book.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * , oid FROM addresses")
    records = cursor.fetchall()
    print(records)

    # create a for loop that loops through the results

    # the 0 is the index position of each record

    # the records contain integers so they have to be converted to a string

    # we can add index positions after record in either the for

    # or the string section to pull either specific records

    # or specific lines in each record

    # in this case, we can pull either only first names or last names etc

    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " - - " + str(record[6])+ "\n"

    queryLabel = Label(root, text=print_records)
    queryLabel.grid(row=11, column=0, columnspan=2)

    conn.commit()
    conn.close()



queryButton = Button(root, text = "Show Records", command = query)
queryButton.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)




# Create a function to delete

def delete():
    conn = sqlite3.connect('address_book.db')
    cursor = conn.cursor()

    # Delete
    cursor.execute("DELETE from addresses WHERE oid = " + deletebox.get())
    #cursor.execute("DELETE from address WHERE f_name=John")

    conn.commit()
    conn.close()


# Create a delete button


deleteButton = Button(root, text = "Delete Record", command = delete)
deleteButton.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=135)


# create a save function for the save button within the edit button

def save():
    conn = sqlite3.connect('address_book.db')
    cursor = conn.cursor()

    record_id = deletebox.get()

    # This updates the table which has slightly different names

    # It is asking the database to update the specific table
    # called addresses only where the oid is equal to an
    # oid that we will define, aka the record number

    

    cursor.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""",
        {
        'first': f_name_editor.get(),
        'last': l_name_editor.get(),
        'address': address_editor.get(),
        'city': city_editor.get(),
        'state': state_editor.get(),
        'zipcode': zip_editor.get(),
        'oid': record_id
        })
       
    conn.commit()
    conn.close()

    editor.destroy()


# Create an edit button and function

# Also creating a new window

# Where we had previously put 'root' to create the main window
# we are now changing the variable to editor = Tk() to generate
# a new window


def edit():
    
    # make this global so that we can reference it in other functions

    global editor

    # This sets up a new window when the function is called

    editor = Tk()
    editor.title('Edit a Record')
    editor.geometry("400x400")

    # This establishes connection to databases and creates the cursor

    conn = sqlite3.connect('address_book.db')
    cursor = conn.cursor()

    record_id = deletebox.get()

    # This is retrieving everything * from the database

    # and then saying that the oid in the database is equal to the variable record_id

    # and we created the variable record_id to be the same as whatever is entered into

    # the deletebox

    cursor.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = cursor.fetchall()

    # All this does is print the records in terminal

    # Which I find useful to make sure they are still in the database

    print(records)

    # Create global variables for text box names so we can use them
    # outside of the function

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zip_editor


    # Create entry boxes specific to the editor window that we created and opened

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10,0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)

    zip_editor = Entry(editor, width=30)
    zip_editor.grid(row=5, column=1, padx=20)

    # create text box labels same as above

    fnameLabel = Label(editor, text="First Name")
    fnameLabel.grid(row=0, column=0, pady=(10,0))

    lnameLabel = Label(editor, text="Last Name")
    lnameLabel.grid(row=1, column=0)

    addressLabel = Label(editor, text="Address")
    addressLabel.grid(row=2, column=0)

    cityLabel = Label(editor, text="City")
    cityLabel.grid(row=3, column=0)

    stateLabel = Label(editor, text="State")
    stateLabel.grid(row=4, column=0)

    zipLabel = Label(editor, text="Zip")
    zipLabel.grid(row=5, column=0)

    # Loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zip_editor.insert(0, record[5])

    # This is a button within a function, so it shows up when the new window is opened

    saveButton = Button(editor, text = "Save Record", command = save)
    saveButton.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=135)



editButton = Button(root, text = "Edit Record", command = edit)
editButton.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

'''

# I might add this disclaimer because the edit button won't work if you don't 

# put an ID number in before opening the edit window

editdisclaimerLabel = Label(root, text="A Record ID Must Be Selected")
editdisclaimerLabel.grid(row=13, column=0)
'''



# Create a Save button to go into the editor record







# commit changes

conn.commit()






# close connection

conn.close()



root.mainloop()