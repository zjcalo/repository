from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import sqlite3

import mysql.connector

import csv

import numpy as np
import matplotlib.pyplot as plt

import requests
import json


from tkinter import ttk



root = Tk()
root.title('CRM App')
root.geometry("700x700")



# Create a database, connection and what is being passed through it

# add the database = after the database has been created

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Zaq12233",
        database = "crmdatabase"
)


# Check to see if connection to mysql is created

print(mydb)

# <mysql.connector.connection_cext.CMySQLConnection object at 0x7ffa56268520>


# Create a cursor in the database and initialize

cursor = mydb.cursor()

# Create a database

'''
cursor.execute("CREATE DATABASE crmdatabase")



cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)
'''

# Create a table

# VARCHAR = text, other data types are specific to mysql

# and then comment out so we don't see the table every time


'''
cursor.execute("CREATE TABLE customers (first_name VARCHAR(255), \
    last_name VARCHAR(255), \
    zipcode INT(10), \
    price_paid DECIMAL(10, 2), \
    user_id INT AUTO_INCREMENT PRIMARY KEY)")
'''

# ALTER TABLE if you want to add additional fields in
'''
cursor.execute("ALTER TABLE customers ADD(\
    email VARCHAR(255), \
    address_1 VARCHAR(255), \
    address_2 VARCHAR(255), \
    city VARCHAR(255), \
    state VARCHAR(255), \
    country VARCHAR(255), \
    phone VARCHAR(255), \
    payment_method VARCHAR(255), \
    discount_code VARCHAR(255))")
'''


# A table can also be created like this initially
# so that it doesn't have to be commented out and
# it will only create a table if it doesn't already exist

'''
cursor.execute("CREATE TABLE IF NOT EXISTS customers (first_name VARCHAR(255), \
    last_name VARCHAR(255), \
    zipcode INT(10), \
    price_paid DECIMAL(10, 2), \
    user_id INT AUTO_INCREMENT PRIMARY KEY)")
'''



# this will validate that the table has been created in the database correctly
'''
cursor.execute("SELECT * from customers")
print(cursor.description)


for a in cursor.description:
    print(a)

'''




# Create a Label


title_label = Label(root, text="Customer Database", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)



# Create a main form to enter customer data

firstnameLabel = Label(root, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
lastnameLabel = Label(root, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
address1Label = Label(root, text="Address 1").grid(row=3, column=0, sticky=W, padx=10)
address2Label = Label(root, text="Address 2").grid(row=4, column=0, sticky=W, padx=10)
cityLabel = Label(root, text="City").grid(row=5, column=0, sticky=W, padx=10)
stateLabel = Label(root, text="State").grid(row=6, column=0, sticky=W, padx=10)
zipcodeLabel = Label(root, text="Zipcode").grid(row=7, column=0, sticky=W, padx=10)
countryLabel = Label(root, text="Country").grid(row=8, column=0, sticky=W, padx=10)
phoneLabel = Label(root, text="Phone").grid(row=9, column=0, sticky=W, padx=10)
emailLabel = Label(root, text="Email").grid(row=10, column=0, sticky=W, padx=10)
usernameLabel = Label(root, text="Username").grid(row=11, column=0, sticky=W, padx=10)
paymentmethodLabel = Label(root, text="Payment Method").grid(row=12, column=0, sticky=W, padx=10)
discountcodeLabel = Label(root, text="Discount").grid(row=13, column=0, sticky=W, padx=10)
pricdepaidLabel = Label(root, text="Price Paid").grid(row=14, column=0, sticky=W, padx=10)



# Create entry boxes

firstnameEntry = Entry(root)
firstnameEntry.grid(row=1, column=1)

lastnameEntry = Entry(root)
lastnameEntry.grid(row=2, column=1, pady=5)

address1Entry = Entry(root)
address1Entry.grid(row=3, column=1, pady=5)

address2Entry = Entry(root)
address2Entry.grid(row=4, column=1, pady=5)

cityEntry = Entry(root)
cityEntry.grid(row=5, column=1, pady=5)

stateEntry = Entry(root)
stateEntry.grid(row=6, column=1, pady=5)

zipcodeEntry = Entry(root)
zipcodeEntry.grid(row=7, column=1, pady=5)

countryEntry = Entry(root)
countryEntry.grid(row=8, column=1, pady=5)

phoneEntry = Entry(root)
phoneEntry.grid(row=9, column=1, pady=5)

emailEntry = Entry(root)
emailEntry.grid(row=10, column=1, pady=5)

usernameEntry = Entry(root)
usernameEntry.grid(row=11, column=1, pady=5)

paymentmethodEntry = Entry(root)
paymentmethodEntry.grid(row=12, column=1, pady=5)

discountcodeEntry = Entry(root)
discountcodeEntry.grid(row=13, column=1, pady=5)

pricepaidEntry = Entry(root)
pricepaidEntry.grid(row=14, column=1, pady=5)


# Create functions

def clearfields():
    firstnameEntry.delete(0,END)
    lastnameEntry.delete(0,END)
    address1Entry.delete(0,END)
    address2Entry.delete(0,END)
    cityEntry.delete(0,END)
    stateEntry.delete(0,END)
    zipcodeEntry.delete(0,END)
    countryEntry.delete(0,END)
    phoneEntry.delete(0,END)
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    paymentmethodEntry.delete(0,END)
    discountcodeEntry.delete(0,END)
    pricepaidEntry.delete(0,END)

'''
first_name, last_name, zipcode, price_paid, user_id, email, address_1, address_2, city, state, country, phone, payment_method, discount_code
'''
def addcustomer():
    
    # the INSERT INTO are all the variables from the table 
    # at the top of the codebase
    
    # The %s is a placeholder for the values that will 
    # later get inserted when they are matched with the 
    # textbox entries

    sqlcommand = "INSERT INTO customers (first_name, last_name, zipcode, price_paid, user_id, email, address_1, address_2, city, state, country, phone, payment_method, discount_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    # These need to line up exactly to the order above
    
    values = (firstnameEntry.get(), lastnameEntry.get(), zipcodeEntry.get(), pricepaidEntry.get(), usernameEntry.get(), emailEntry.get(), address1Entry.get(), address2Entry.get(), cityEntry.get(), stateEntry.get(), countryEntry.get(), phoneEntry.get(), paymentmethodEntry.get(), discountcodeEntry.get())

    cursor.execute(sqlcommand, values)

    # commit changes to the database

    mydb.commit()
    clearfields()


def writeToCsv(result):
    with open('customers.csv', 'a') as f:
        w = csv.writer(f, dialect='excel')
        for record in result:
            w.writerow(record)



def listCustomers():
    
    # Create a new window

    listCustomerQuery = Tk()
    listCustomerQuery.title("List All Customers")
    listCustomerQuery.geometry("800x800")

    # Query the database EX 1
    '''
    cursor.execute("SELECT * FROM customers")
    result = cursor.fetchall()
    for x in result:
        # Below is a way to generically display everything
        lookupLabel = Label(listCustomerQuery, text=x)
        lookupLabel.pack()

        # Can add an index number to x to 
        # only display specific variables from the database list

        # Ex:

        # lookupLabel = Label(listCustomerQuery, text=x[0])
    '''

    # Query the database, more specific

    cursor.execute("SELECT * FROM customers")
    result = cursor.fetchall()

    # creates an enumerated for loop
    # every item gets a number, index associated with it

    for index, x in enumerate(result):

        # Creates a variable num that is = 0 so that we can
        # use it as a reference to position every subsequent
        # database set that gets printed out

        num = 0

        # this picks up each individual item in the database
        # gives it a label equal to its value, 'y'
        # and then grids it based on its index value
        # and its next num value

        for y in x:
            lookupLabel = Label(listCustomerQuery, text=y)
            lookupLabel.grid(row=index, column=num)
            num += 1

    csvButton = Button(listCustomerQuery, text="Save to Excel", command = lambda: writeToCsv(result))
    csvButton.grid(row=index + 1, column=0)


def searchCustomers():

    # Create a new window

    searchCustomerQuery = Tk()
    searchCustomerQuery.title("Search All Customers")
    searchCustomerQuery.geometry("1400x900")


    # the update function which replaces the items in the database with the new ones
    
    def update():
        

        sqlCommand ="""UPDATE customers SET first_name = %s, last_name = %s, zipcode = %s, price_paid = %s, user_id = %s, email = %s, address_1 = %s, address_2 = %s, city = %s, state = %s, country = %s, phone = %s, payment_method = %s, discount_code = %s WHERE user_id = %s"""

        # this GETS whatever we typed into the entry boxes that pop up
        # on the edit screen and then assigns them to the 
        # first_name last_name etcetera variables that are defined here

        first_name = firstnameEntry2.get()
        last_name = lastnameEntry2.get()
        zipcode = zipcodeEntry2.get()
        price_paid = pricepaidEntry2.get()
        user_id = usernameEntry2.get()
        email = emailEntry2.get()
        address_1 = address1Entry2.get()
        address_2 = address2Entry2.get()
        city = cityEntry2.get()
        state = stateEntry2.get()
        country = countryEntry2.get()
        phone = phoneEntry2.get()
        payment_method = paymentmethodEntry2.get()
        discount_code =  discountcodeEntry2.get()

        id_value = usernameEntry2.get()

        inputs = (first_name, last_name, zipcode, price_paid, user_id, email, address_1, address_2, city, state, country, phone, payment_method, discount_code, id_value)

        cursor.execute(sqlCommand, inputs)
        mydb.commit()
        searchCustomerQuery.destroy()

    # Define editNow so it can be used in the button further down

    def editNow(id, index):
        
        sql2 = "SELECT * FROM customers WHERE user_id = %s"
        name2 = (id, )
        result2 = cursor.execute(sql2, name2)
        result2 = cursor.fetchall()
        
        # this makes sure that the correct record is referenced when
        # we select the edit button
        
        print(result2)
        
        # We are only doing this for formatting reasons so that
        # the new fields we are entering do not overlap with
        # existing buttons
        
        index += 1

        # Create a main form to enter customer data

        firstnameLabel = Label(searchCustomerQuery, text="First Name").grid(row=index+1, column=0, sticky=W, padx=10, pady=10)
        lastnameLabel = Label(searchCustomerQuery, text="Last Name").grid(row=index+2, column=0, sticky=W, padx=10)
        address1Label = Label(searchCustomerQuery, text="Address 1").grid(row=index+3, column=0, sticky=W, padx=10)
        address2Label = Label(searchCustomerQuery, text="Address 2").grid(row=index+4, column=0, sticky=W, padx=10)
        cityLabel = Label(searchCustomerQuery, text="City").grid(row=index+5, column=0, sticky=W, padx=10)
        stateLabel = Label(searchCustomerQuery, text="State").grid(row=index+6, column=0, sticky=W, padx=10)
        zipcodeLabel = Label(searchCustomerQuery, text="Zipcode").grid(row=index+7, column=0, sticky=W, padx=10)
        countryLabel = Label(searchCustomerQuery, text="Country").grid(row=index+8, column=0, sticky=W, padx=10)
        phoneLabel = Label(searchCustomerQuery, text="Phone").grid(row=index+9, column=0, sticky=W, padx=10)
        emailLabel = Label(searchCustomerQuery, text="Email").grid(row=index+10, column=0, sticky=W, padx=10)
        usernameLabel = Label(searchCustomerQuery, text="Username").grid(row=index+11, column=0, sticky=W, padx=10)
        paymentmethodLabel = Label(searchCustomerQuery, text="Payment Method").grid(row=index+12, column=0, sticky=W, padx=10)
        discountcodeLabel = Label(searchCustomerQuery, text="Discount").grid(row=index+13, column=0, sticky=W, padx=10)
        pricdepaidLabel = Label(searchCustomerQuery, text="Price Paid").grid(row=index+14, column=0, sticky=W, padx=10)
        
        # Create entry boxes and make them global

        # we also add the .insert which replaces the 
        # blank entry box with the text from the result2 
        # for loop we created above with each specific 
        # indexed entry in the list which is also why 
        # we printed the list out in the terminal

        global firstnameEntry2
        firstnameEntry2 = Entry(searchCustomerQuery)
        firstnameEntry2.grid(row=index+1, column=1, pady=10)
        firstnameEntry2.insert(0, result2[0][0])
        
        global lastnameEntry2
        lastnameEntry2 = Entry(searchCustomerQuery)
        lastnameEntry2.grid(row=index+2, column=1, pady=5)
        lastnameEntry2.insert(0, result2[0][1])
        
        global address1Entry2
        address1Entry2 = Entry(searchCustomerQuery)
        address1Entry2.grid(row=index+3, column=1, pady=5)
        address1Entry2.insert(0, result2[0][6])
        
        global address2Entry2
        address2Entry2 = Entry(searchCustomerQuery)
        address2Entry2.grid(row=index+4, column=1, pady=5)
        address2Entry2.insert(0, result2[0][7])
        
        global cityEntry2
        cityEntry2 = Entry(searchCustomerQuery)
        cityEntry2.grid(row=index+5, column=1, pady=5)
        cityEntry2.insert(0, result2[0][8])
        
        global stateEntry2
        stateEntry2 = Entry(searchCustomerQuery)
        stateEntry2.grid(row=index+6, column=1, pady=5)
        stateEntry2.insert(0, result2[0][9])
        
        global zipcodeEntry2
        zipcodeEntry2 = Entry(searchCustomerQuery)
        zipcodeEntry2.grid(row=index+7, column=1, pady=5)
        zipcodeEntry2.insert(0, result2[0][2])
        
        global countryEntry2
        countryEntry2 = Entry(searchCustomerQuery)
        countryEntry2.grid(row=index+8, column=1, pady=5)
        countryEntry2.insert(0, result2[0][10])
        
        global phoneEntry2
        phoneEntry2 = Entry(searchCustomerQuery)
        phoneEntry2.grid(row=index+9, column=1, pady=5)
        phoneEntry2.insert(0, result2[0][11])
        
        global emailEntry2
        emailEntry2 = Entry(searchCustomerQuery)
        emailEntry2.grid(row=index+10, column=1, pady=5)
        emailEntry2.insert(0, result2[0][5])
        
        global usernameEntry2
        usernameEntry2 = Entry(searchCustomerQuery)
        usernameEntry2.grid(row=index+11, column=1, pady=5)
        usernameEntry2.insert(0, result2[0][4])
        
        global paymentmethodEntry2
        paymentmethodEntry2 = Entry(searchCustomerQuery)
        paymentmethodEntry2.grid(row=index+12, column=1, pady=5)
        paymentmethodEntry2.insert(0, result2[0][12])
        
        global discountcodeEntry2
        discountcodeEntry2 = Entry(searchCustomerQuery)
        discountcodeEntry2.grid(row=index+13, column=1, pady=5)
        discountcodeEntry2.insert(0, result2[0][13])
        
        global pricepaidEntry2
        pricepaidEntry2 = Entry(searchCustomerQuery)
        pricepaidEntry2.grid(row=index+14, column=1, pady=5)
        pricepaidEntry2.insert(0, result2[0][3])
    

        saveRecord = Button(searchCustomerQuery, text="Update Record", command=update)
        saveRecord.grid(row=index+15, column=0, padx=10)


    # Define the searchNow function before it
    # is used in the button lower down

    def searchNow():
        
        # this GETS whatever is selected in the drop down box
        # and recognizes the text

        selected = drop.get()
        if selected == "Search by":
            test = Label(searchCustomerQuery, text="Hey! You didn't select anything")
            test.grid(row=3, column=0)
        if selected == "Last Name":
            sql = "SELECT * FROM customers WHERE last_name = %s"
            test = Label(searchCustomerQuery, text="Hey! last name")
            test.grid(row=3, column=0)
        if selected == "Email Address":
            sql = "SELECT * FROM customers WHERE email = %s"
            test = Label(searchCustomerQuery, text="Hey! email")
            test.grid(row=3, column=0)
        if selected == "Customer ID":
            sql = "SELECT * FROM customers WHERE user_id = %s"
            test = Label(searchCustomerQuery, text="Hey! customer id")
            test.grid(row=3, column=0)
        
        
        searched = searchBox.get()
        #sql = "SELECT * FROM customers WHERE last_name = %s"
        name = (searched, )
        result = cursor.execute(sql, name)
        result = cursor.fetchall()

        if not result:
            result = "Record Not Found..."
            searchedLabel = Label(searchCustomerQuery, text=result)
            searchedLabel.grid(row=2, column=0)
        else:
       
        # same as in the list customer function 
        # except some aspects of it are changed 
        # to work within the search parameters
        
            for index, x in enumerate(result):
                num = 0
            
            # we have to do the += 2 on the index 
            # because the index is going to default 
            # to starting at 0 but we already have 
            # content in the grid at row 0 so we have 
            # to make sure that the items that show up 
            # do not overlap or it won't look right
            
                index += 2

                # the idReference pulls the 4th item in the list 
                # that is returned and since we created x as the 
                # variable for the list that gets returned we have 
                # to use x[4] to reference the 4th item in the list 
                # which is actually the user ID which is the way 
                # we are going to be referencing the specific 
                # database entry we are editing

                # also it has to be converted to a string

                idReference = str(x[4])

                # Create an Edit Button for each entry 
                # in the database that shows up when 
                # we search for it

                editButton = Button(searchCustomerQuery, text="Edit " + idReference, command = lambda: editNow(idReference, index))
                editButton.grid(row=index, column=num)
                
                
                
                for y in x:
                    searchedLabel = Label(searchCustomerQuery, text=y)
                    searchedLabel.grid(row=index, column=num+1)
                    num += 1


            csvButton = Button(searchCustomerQuery, text="Save to Excel", command = lambda: writeToCsv(result))
            csvButton.grid(row=index + 1, column=0)

        #searchedLabel = Label(searchCustomerQuery, text=result)
        #searchedLabel.grid(row=4, column=0, padx=10, pady=10)
        
    # Entry box to search

    searchBox = Entry(searchCustomerQuery)
    searchBox.grid(row=0, column=1, padx=10, pady=10)

    # Drop down box

    drop = ttk.Combobox(searchCustomerQuery, value=["Search by...", "Last Name", "Email Address", "Customer ID"])
    drop.current(0)
    drop.grid(row=0, column=2, padx=10, pady=10)

    # Entry box label

    searchBoxLabel = Label(searchCustomerQuery, text="Search")
    searchBoxLabel.grid(row=0, column=0, padx=10, pady=10)

    # Entry box search button

    searchBoxButton = Button(searchCustomerQuery, text="Search Customers", command = searchNow)
    searchBoxButton.grid(row=1, column=0, padx=10, pady=10)

# Create buttons

addcustomerButton = Button(root, text="Add Customer To Database", command=addcustomer)
addcustomerButton.grid(row=15, column=0, padx=10, pady=10)


clearfieldsButton = Button(root, text="Clear Fields", command=clearfields)
clearfieldsButton.grid(row=15, column=1)


# List customers buttom

listCustomerButton = Button(root, text="List Customers", command=listCustomers)
listCustomerButton.grid(row=16, column=0, sticky=W, padx=10)

# Search button

searchButton = Button(root, text="Search / Edit Customers", command=searchCustomers)
searchButton.grid(row=16, column=1, sticky=W, padx=10)


cursor.execute("SELECT * FROM customers")
result = cursor.fetchall()
for x in result:
    print(x)




 
root.mainloop()