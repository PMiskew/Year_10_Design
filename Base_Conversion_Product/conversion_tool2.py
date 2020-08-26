import tkinter as tk

print("Stage 2")

'''
This event driven function is called when
return is pressed
'''
def process(*args):
	print("Process Called")

	val = ent_value.get()
	print(val)
	#Check to ensure string of 1's and 0's



	#If valid Convert to Base 10
		#Remove left most 0
		#Convert
		#update display with conversion
	#else
		#update display with error message

	lab_results.config(text = str(val))
	ent_value.delete(0,tk.END)

root = tk.Tk()

lab_instructions = tk.Label(root, text = "Enter Binary")
ent_value = tk.Entry(root)

lab_results = tk.Label(root, text = "--")

lab_instructions.pack()
ent_value.pack()
lab_results.pack()


root.bind("<Return>",process)
root.mainloop()