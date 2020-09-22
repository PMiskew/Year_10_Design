import requests
import json
from pprint import pprint
import tkinter as tk


#Get Key
#This is a file not in my respository I don't want you to have it
file = open("..//..//API_Keys//fixerkey.txt","r")

key = file.read()


resp = requests.get('http://data.fixer.io/api/latest?access_key='+key)
#resp = requests.get('https://jsonplaceholder.typicode.com/comments')


#Converts response to JSON
data = resp.json()

#pprint(data)
#print(data["timestamp"])
#print(data["base"])
#print(data["rates"]["CAD"])

country = []
value = []

#loops through the dictionary at data["rates"]
for key in data["rates"]:
	#print(key,":",data["rates"][key])

	country.append(key) #append the key into country list
	value.append(data["rates"][key]) #append the value into value list

print(country)
print(value)


def change(x):
	print(x)
	print(data["rates"][x])

root = tk.Tk() #Creates my main window for GUI program
#Build in here
#	Step 1: Construct the widget/object
#	Step 2: Configure widget/object
#	Step 3: Place it on the frame/main window

lab = tk.Label(root, text = "Select Currency") #construction 

var = tk.StringVar(root)
var.set(country[0])
option_menu = tk.OptionMenu(root, var, *country, command = change)

lab.pack() #placing
option_menu.pack()




root.mainloop() #Executes an infitie loop waiting for the use to do something
print("END")














