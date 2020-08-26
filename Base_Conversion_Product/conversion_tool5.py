import tkinter as tk

print("Stage 4")

'''
This event driven function is called when
return is pressed
'''
def process(*args):
	print("Process Called")

	val = ent_value.get()
	print(val)
	#Check to ensure string of 1's and 0's
	check = check01(val)
	print(check)
	

	if (check):
		#Remove left most 0
		val = remove0(val)
		print(val)
		#Convert
		result = base2to10(val)
		#update display with conversion
		lab_results.config(text = str(val) + " --> " + str(result))
	else:
		#update display with error message
		lab_results.config(text = "INVALID INPUT")
	

	ent_value.delete(0,tk.END)


def base2to10(str):

	
	n = 0
	total = 0

	for i in range(len(str) - 1, -1, -1):
		print("***",n)
		total = total + int(str[i]) * (2**n)
		print("---",total)
		n = n + 1

	return total


'''
This method takes a string and checks to see that
it only contains 0's and 1's.  
Returns true if only 0's and 1's false otherwise
'''
def check01(str):

	
	num_0 = str.count("0")
	num_1 = str.count("1")

	if (num_0 + num_1 == len(str)):
		return True
	return False
	
	#One Liner
	#return (str.count("0")+str.count("1") == len(str))

'''
This function takes finds the first 1 and
removes all characters to the left.

precondition: str only contains 0's and 1's
'''
def remove0(str):

	for i in range(0, len(str),1):
		if str[i] == "1":
			return str[i:]

	return str

root = tk.Tk()

lab_instructions = tk.Label(root, text = "Enter Binary")
ent_value = tk.Entry(root)

lab_results = tk.Label(root, text = "--")

lab_instructions.pack()
ent_value.pack()
lab_results.pack()


root.bind("<Return>",process)
root.mainloop()