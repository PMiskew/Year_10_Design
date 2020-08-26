import tkinter as tk

print("Stage 4")


def process(*args):
	
	val = ent_value.get()
	


	#Check to ensure string of 1's and 0's
	check = check01(val)
	


	if (check == True):
		val = remove0(val)
		#Conversions
		lab_results.config(text = "VALID INPUT"+val)
	else:
		lab_results.config(text = "INVALID")

	ent_value.delete(0,tk.END)

def remove0(str):

	'''
	012345
	000101
	'''
	for i in range(0, len(str),1):
		if (str[i] == "1"):
			return str[i:]

	return str


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