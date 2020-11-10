import tkinter as tk

uNames = ["user1@test.com","user2@test.com","user3@test.com"]
pWords = ["pword1","pword2","pword3"]
active = ["",""] #Stores active user 

def checkCred(*arg):

	print("Checking")

	#Write the code to
	#Step 1: Take entry for user name
	u = entunLF.get()
	#Step 2: Take entry for password
	p = entpwLF.get()
	#Step 3: Loop through usernames and check if valid with password

	for i in range(0,len(uNames),1):
		if (uNames[i] == u):
			if (pWords[i] == p):
				#SWAP SCREENS
				loginFrame.pack_forget()
				homeFrame.pack()
				#SET ACTIVE USER
				active[0] = u
				active[1] = p
				entunLF.delete(0,tk.END)
				entpwLF.delete(0,tk.END)
				return

	#If the username nad password is correct swap frames. 
	entunLF.delete(0,tk.END)
	entpwLF.delete(0,tk.END)

def logout(*args): 
	#SWAP
	loginFrame.pack()
	homeFrame.pack_forget()

	#REMOVE ACTIVE USER
	active[0] = ""
	active[1] = ""

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
logoutHF = tk.Button(homeFrame, text = "logout",command = logout)
labHF.pack()
logoutHF.pack()



loginFrame.pack()
root.mainloop()
print("END PROGRAM")