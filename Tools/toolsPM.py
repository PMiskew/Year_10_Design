'''
isEven takes a single integer parameter a >= 0 returning true
if a is even and false if a is odd
'''
def isEven(a):

	if a % 2 == 0:
		return True

	return False

'''
Codingbat Problem
'''
def missing_char(str, n):
  
	front = str[0:n]
	back = str[n + 1:]
	result = front + back
	return result



#Test Code for missing_char

print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))


#Test Code for isEven
'''
print(isEven(0))
print(isEven(10))
print(isEven(9))

for i in range(0, 100, 1):
	print(str(i)+" is "+str(isEven(i)))
'''
