import tkinter as tk

print("Stage 2")


def process(*args):
	print("process")

	val = ent_value.get()
	print(val)


	#Check to ensure string of 1's and 0's



	#If val is valid 
		#Remove left most 0
		#Conversions
		#update display with conversion
	#else:
		#update display with error message

	ent_value.delete(0,tk.END)

root = tk.Tk()

#Construct the widgets
lab_instructions = tk.Label(root, text = "Enter Binary")
ent_value = tk.Entry(root)
lab_results = tk.Label(root, text = "--")

#Configure Widgets

#Add the widgets to the window
lab_instructions.pack()
ent_value.pack()
lab_results.pack()

root.bind("<Return>",process)
root.mainloop()