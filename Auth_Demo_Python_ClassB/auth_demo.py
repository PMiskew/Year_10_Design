import tkinter as tk

uNames = ["user1@test.com"]
pWords = ["pword1"]


def checkCred(*arg):

	print("Checking")

	#Write the code to
	#Step 1: Take entry for user name
	#Step 2: Take entry for password
	#Step 3: Loop through usernames and check if valid with password

	#If the username nad password is correct swap frames. 
	loginFrame.pack_forget()
	homeFrame.pack()

root = tk.Tk() #Creates your main window

#Build a login frame
loginFrame = tk.Frame(root)

labunLF = tk.Label(loginFrame,text = "User Name:")
entunLF = tk.Entry(loginFrame, width = 20)

labpwLF = tk.Label(loginFrame,text = "Password")
entpwLF = tk.Entry(loginFrame, width = 20)

submitLF = tk.Button(loginFrame, text = "Submit", command = checkCred)

labunLF.pack()
entunLF.pack()

labpwLF.pack()
entpwLF.pack()

submitLF.pack()

#Build a home page frame
homeFrame = tk.Frame(root)

labHF = tk.Label(homeFrame, text = "Welcome to Soccer Magic")

labHF.pack()



loginFrame.pack()
root.mainloop()
print("END PROGRAM")