import requests
import json

import tkinter as tk

#MYP POINT - This 

country = []
value = []


def change(x):
	i= country.index(x)
	print(value[i])

	print()

#Get Key
#This is a file not in my respository I don't want you to have it
file = open("..//..//API_Keys//fixerkey.txt","r")

key = file.read()


resp = requests.get('http://data.fixer.io/api/latest&USD?access_key='+key)

#Converts response to JSON
data = resp.json()["rates"]




for key in data:
	country.append(key)
	value.append(data[key])


#*************************************************************************
root = tk.Tk()

cur_label = tk.Label(root, text = "Select Currency")
variable = tk.StringVar(root)
variable.set(country[0]) # d
cur_select = tk.OptionMenu(root, variable, *country, command = change)

cur_label.pack()
cur_select.pack()

root.mainloop()
