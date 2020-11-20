import tkinter as tk

#Task:

'''
Add a label at teh top with a title.  I want the font to bigger
(BUILD A LABEL)
See if you can modify the textbox so that it is more visible by
playing with the border

CAUTION - DON"T TRY AND CHANCE THE COLOR OF THE BUTTONS

Can you bind a different function to the buttons
'''
#DATA - All the data needs to be stored in lists



#FUNCTIONS

#GUI
#Assignment Statment
root = tk.Tk() #Creates the window 

#Step 1: Construct the object

'''
With python and other languages we have parameters based on order
and named parameters (order doesn't matter)
'''
searchBar = tk.Entry(root,width = 30)

display1 = tk.Label(root,text = "IMAGE 1")
display2 = tk.Label(root,text = "IMAGE 2")

btn1 = tk.Button(root,text = "LEARN MORE - EPL")
btn2 = tk.Button(root,text = "LEARN MORE - Seria")

display = tk.Text(root,width = 30, height = 10)

#Step2: Configure the object (Not always done)
#searchBar.config(state = tk.DISABLED)
display.config(state = tk.DISABLED)

#Step 3: Place the widget
'''
There are multiple ways to place objects on a tkinter layout
 - pack
 - grid
 - place
'''

searchBar.grid(row = 0, column = 0, columnspan = 2)
display1.grid(row = 1, column = 0)
display2.grid(row = 1, column = 1)
btn1.grid(row = 2, column = 0)
btn2.grid(row = 2, column = 1)

display.grid(row = 3, column = 0, columnspan = 2)



'''
This is event driven programming
We set everything up and we tell the program to wait for something to 
happen.
Sometimes you hear people call a "game loop"  
'''

root.mainloop() #launches your window and sits here waiting
print("End Program")
