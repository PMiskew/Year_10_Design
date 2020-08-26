import tkinter as tk

print("Stage 3")


def process(*args):
	
	val = ent_value.get()
	


	#Check to ensure string of 1's and 0's
	check = check01(val)
	


	if (check == True):
		#Remove left most 0
		#Conversions
		lab_results.config(text = "VALID INPUT")
	else:
		lab_results.config(text = "INVALID")

	ent_value.delete(0,tk.END)

def check01(str):
	
	num_0 = str.count("0")
	num_1 = str.count("1")

	if num_0 + num_1 == len(str):
		return True
	return False

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