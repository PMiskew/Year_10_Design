import tkinter as tk
import requests
from pprint import pprint
import random


resp = requests.get("https://raw.githubusercontent.com/PMiskew/Year_10_Design/master/Extra_Help_PullingFromJSON/data.json")
data = resp.json()
#pprint(data)

#What we woudl do is read in all the questions and then use them to 
#populate my tkinter

questions = []
answers = []

#Taking the JSON data and putting into hte lists questions and answers
#so you can use it in your program
for i in range(0, len(data),1):
	print(data[i]["question"])
	questions.append(data[i]["question"])
	answers.append(data[i]["answer"])

#Set up your tkineter and when you want to display questions use the 
#the list questions

def next(*args):
	print("Next")

	#generate a random number from 0 to len(questions)
	x = random.randint(0,len(questions) - 1)
	print(x)
	label.config(text = questions[x])

root = tk.Tk()

label = tk.Label(root,text = questions[0])
label.pack()

btn = tk.Button(root, text = "NEXT", command = next)
btn.pack();



root.mainloop()


