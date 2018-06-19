"""Author : Mohammad Shakoory"""
# Question 6

import json
from Tkinter import *
from ttk import *

# Dictionary to save city names as keys and relevant index in data(list of dictionaries)
mapped_data = {}

# Load json file into data variable(list)
with open('ca.json') as json_data:
    data = json.load(json_data)

# Mapping city names and index of them in data(list)
for i in range(len(data)):
    if data[i]["full_county_name"] is not None:
        mapped_data[data[i]['name']] = i


class Application(Frame):
    """Class to create appropriate widgets: combobox, labels and text boxes"""

    def __init__(self, master=None):
        """ Initialize the frame"""
        Frame.__init__(self, master)
        self.grid()
        self.create_boxes()

    def create_boxes(self):
        """create widgets: combobox, labels and text boxes"""

        self.box = Combobox(self.master, state="readonly", width=49)    # creating a combobox which shows city names
        self.box['values'] = (mapped_data.keys())
        self.box.bind("<<ComboboxSelected>>", self.show_data)
        self.box.grid(row=0, column=0, sticky=N, pady=15, padx=(78, 0))

        self.l1 = Label(self, text="City")  # creating labels
        self.l1.grid(row=0, column=0, sticky=W, pady=15, padx=10)
        self.l2 = Label(self, text="County")
        self.l2.grid(row=1, column=0, sticky=W, pady=15, padx=10)
        self.l3 = Label(self, text="Latitude")
        self.l3.grid(row=2, column=0, sticky=W, pady=15, padx=10)
        self.l4 = Label(self, text="Longitude")
        self.l4.grid(row=3, column=0, sticky=W, pady=15, padx=10)

        self.t1 = Text(self, height=1, width=39)    # creating text boxes
        self.t1.grid(row=1, column=1, pady=15, padx=40)
        self.t2 = Text(self, height=1, width=39)
        self.t2.grid(row=2, column=1, pady=15, padx=40)
        self.t3 = Text(self, height=1, width=39)
        self.t3.grid(row=3, column=1, pady=15, padx=40)

    def show_data(self, event):
        """Function to insert the data for county name, latitude and longitude in text boxes t1, t2 and t3 """
        self.t1.delete(0.0, END)    # Delete each box before inserting a new value
        self.t2.delete(0.0, END)
        self.t3.delete(0.0, END)

        city_name = self.box.get()  # getting the chosen city name from the combobox

        self.t1.insert(END, data[mapped_data[city_name]]["full_county_name"])   # Insert the results
        self.t2.insert(END, data[mapped_data[city_name]]["primary_latitude"])
        self.t3.insert(END, data[mapped_data[city_name]]["primary_longitude"])


# Create the window
root = Tk()

# Modify the window
root.title('City Information')
root.geometry('460x215')
app = Application(root)

# Event loop
root.mainloop()

