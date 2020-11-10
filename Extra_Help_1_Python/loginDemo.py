import tkinter as tk

#STEP 1: ACCESS FILES AND STORE IN MY LISTS FOR PROGRAM
#Dealing with Data before starting program
users = []
passwords = []


userFile = open("users.txt","r")
usersRaw = userFile.read()

#When I use the read function it returns everything as a string
users = usersRaw.split("\n")

passFile = open("password.txt","r")

passWordRaw = passFile.read()
passwords = passWordRaw.split("\n")

print(users)
print(passwords)


#Step 2: BUILD PROGRAM AND RUN IT
def register(*args):

	u = entun.get()
	users.append(u)

	p = entpw.get()
	passwords.append(p)

	print(users)
	print(passwords)


def login():
	print("login")


root = tk.Tk()

labun = tk.Label(root,text = "User Name: ")
entun = tk.Entry(root, width = 20)

labpw = tk.Label(root,text = "Password: ")
entpw = tk.Entry(root, width = 20)

labun.pack()
entun.pack()

labpw.pack()
entpw.pack()

#This button makes a new user
btnRegister = tk.Button(root,text = "Register", command = register)
btnLogin = tk.Button(root, text = "Login", command = login)

btnRegister.pack()
btnLogin.pack()







root.mainloop()

#STEP 3: COPY NEW DATA BACK FOR FILES 
#write all the content back to the files
userFile = open("users.txt","w")

for i in range(0,len(users),1):
	userFile.write(users[i]+"\n")

userFile.close()

passFile = open("password.txt","w")

for i in range(0,len(passwords),1):
	passFile.write(passwords[i]+"\n")

passFile.close()

