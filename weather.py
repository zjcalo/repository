from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import sqlite3
sqlite3.paramstyle = 'named'

import requests
import json



root = Tk()
root.title('Weather App')
root.geometry("600x300")



'''

[{"DateObserved":"2021-01-06 ","HourObserved":21,"LocalTimeZone":"EST","ReportingArea":"Boston","StateCode":"MA","Latitude":42.351,"Longitude":-71.051,"ParameterName":"O3","AQI":23,"Category":
{"Number":1,"Name":"Good"}},
{"DateObserved":"2021-01-06 ","HourObserved":21,"LocalTimeZone":"EST","ReportingArea":"Boston","StateCode":"MA","Latitude":42.351,"Longitude":-71.051,"ParameterName":"PM2.5","AQI":23,"Category":
{"Number":1,"Name":"Good"}}]

'''
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=02138&distance=5&API_KEY=EC800CFC-14B9-4A12-A1F0-2D0C6F6C3B19


# Create an API Request

# The "good", "moderate" etc in the category == are coming from airnow.gov
# and they are all the exact wordings from the air quality index scale



# Create zip look up process

zip = Entry(root)
zip.grid(row=0, column=0)

def ziplookup():
    #zip.get()
    #zipLabel = Label(root, text=zip.get())
    #zipLabel.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=25&API_KEY=EC800CFC-14B9-4A12-A1F0-2D0C6F6C3B19")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        latitude = api[0]['Latitude']
        longitude = api[0]['Longitude']
        category = api[0]['Category']['Name']

        # Series of if statements that generate a weather color
        # based on the category output

        if category == "Good":
            weather_color = "#00E400"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups (USG)":
            weather_color = "#FF7E00"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        # This creates the background color of the whole app

        root.configure(background=weather_color)

        # Create a label that pops up and the background color it generates
        # is dependent on the elif statements above based on the string output of the API

        apiLabel = Label(root, text= category + "\n" + city + "\n" + " Air Quality " + str(quality) + "\n" + str(latitude) + str(longitude), font=("Helvetica", 20), background=weather_color)
        apiLabel.grid(row=1, column=0, columnspan=2)
        apiLabel.destroy()

    except Exception as e:
        api = "Error..."

zipButton = Button(root, text = "Look up zipcode", command=ziplookup)
zipButton.grid(row=0, column=1)


# Below is one way to do it

# But it is commented out because we are doing it a different way

'''
# Instead of pulling the full api, we can put in the
# numeric index value in the square brackets to return
# only a section of the list generated


# Then within the index valued list, we can specify a string value
# for which specific values we want to return

apiLabel = Label(root, text=api[0]['ReportingArea'])
apiLabel.pack()
'''

# Here we are adding the variables we created above in the 
# api rewquest into the text read out

# Anything that is a number/integer needs to be converted
# into a string function to work with the text=

'''
apiLabel = Label(root, text= city + "\n" + " Air Quality " + str(quality) + "\n" + str(latitude) + str(longitude), font=("Helvetica", 20), background="green")
apiLabel.pack()
'''


root.mainloop()


'''

This is how it was originally written, but we put it
into a ziplook up function later

try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=93650&distance=25&API_KEY=EC800CFC-14B9-4A12-A1F0-2D0C6F6C3B19")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    latitude = api[0]['Latitude']
    longitude = api[0]['Longitude']
    category = api[0]['Category']['Name']

    # Series of if statements that generate a weather color
    # based on the category output

    if category == "Good":
        weather_color = "#00E400"
    elif category == "Moderate":
        weather_color = "#FFFF00"
    elif category == "Unhealthy for Sensitive Groups (USG)":
        weather_color = "#FF7E00"
    elif category == "Unhealthy":
        weather_color = "#FF0000"
    elif category == "Very Unhealthy":
        weather_color = "#990066"
    elif category == "Hazardous":
        weather_color = "#660000"

    # This creates the background color of the whole app

    root.configure(background=weather_color)

    # Create a label that pops up and the background color it generates
    # is dependent on the elif statements above based on the string output of the API

    apiLabel = Label(root, text= category + "\n" + city + "\n" + " Air Quality " + str(quality) + "\n" + str(latitude) + str(longitude), font=("Helvetica", 20), background=weather_color)
    apiLabel.grid(row=4, column=0)

except Exception as e:
    api = "Error..."
'''