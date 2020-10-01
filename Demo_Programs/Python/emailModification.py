'''
	Step 1: Check for @ symbol
	Step 2: Find the location of the @ symbol
	Step 3: Loop from index 0 to index of @ symbol
		Step3a: If the value is not a . copy to new string
	Step 4: Copy the @ and everything to the right 


'''

'''

'''
def checkEmail(email):

	c = email.count("@")
	return c == 1

def modEmail(email):


	if (checkEmail(email) == False):
		return -1

	index_of_at = email.index("@")
	#print(index_of_at)

	'''
	email = "the.name@gmail.com"
	index_of_at = 8 
	
	i | i < 8      | email[i] != "." | result
	0 | 0 < 8 TRUE | t != .  TRUE    | "t"
	1 | 1 < 8 TRUE | h != .  TRUE    | "th"
	2 | 2 < 8 TRUE | e != .  TRUE    | "the"
	3 | 3 < 8 TRUE | . != .  FALSE   | 
	4 | 4 < 8 TRUE | n != .  TRUE    | "then"
	5 | 5 < 8 TRUE | a != .  TRUE    | "thena"
	6 | 6 < 8 TRUE | m != .  TRUE    | "thenam"
	7 | 7 < 8 TRUE | e != .  TRUE    | "thename"
	8 | 8 < 8 FALSE EXIT LOOP

	'''
	result = ""
	for i in range(0, index_of_at,1):
		if email[i] != ".":
			result = result + email[i]

	result = result + email[index_of_at:len(email)]
	return result




print(modEmail("marshal.wang@gmail.com")) # marshalwang@gmail.com
print(modEmail("m.arshalwang@gmail.com")) # marshalwang@gmail.com
print(modEmail("ma.rshal.wan.g@gmail.com")) # marshalwang@gmail.com
print(modEmail("ma.rshal.wan.g@gma@il.com")) # -1






