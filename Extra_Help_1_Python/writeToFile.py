import tkinter as tk

#Any variables that you want to use place here. 
#They have to be reference types 
l = []

def clicked9():

	
	l.append(9)
	print(l)

def clicked8():
	l.append(8)
	print(l)

root = tk.Tk()

btn9 = tk.Button(root, text ="add 9", command = clicked9)
btn9.pack()


btn8 = tk.Button(root, text ="add 8", command = clicked8)
btn8.pack()

root.mainloop()

#When close the program I want to write the contents of this
#list to a file
#You can toggle between w for write and a for append
file = open("data.txt","w")

for i in range(0, len(l), 1):
	file.write(str(l[i])+"\n")

file.close()







