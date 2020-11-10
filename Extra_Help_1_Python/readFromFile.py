#when you load your program you want to load all the users
#and their passwords

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

