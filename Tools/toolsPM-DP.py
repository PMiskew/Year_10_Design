'''
isEven takes a single integer parameter a >= 0 returning true
if a is even and false if a is odd
'''
def isEven(a):

	if a % 2 == 0:
		return True

	return False
######################################
'''
Codingbat Problem
'''
def missing_char(str, n):
	
	return str[0:n] + str[n + 1:len(str)]
 
###################################### 
def first_last6(nums):
  
  
  if (nums[0] == 6 or nums[len(nums) - 1] == 6):
    return True
  
  return False
  
#######################################
'''
This function takes a single positive integer parameter and returns
the sum of the digits
Parameters: i >= 0
return: returns sum of the digits

preondition: i is a valid integer greater than 0
'''
def sumDigits(a):

	total = 0
	#Casting is the process of changing type. 
	a = str(a)  

	#Fundamental skill: Looping through string

	#Count, check, change
	for i in range(0, len(a),1):
		total = total + int(a[i])

	return total
	#Trace Table:
	# a = "1234"
	# i | i < len(a) | 
	# 0	| 0 < 4 	 |	T RUN LOOP  total = 0 + a[0] = 0 + "1"
	# 1 | 1 < 4		 |  T RUN LOOP  total = 1 + a[1] = 1 + "2"
	# 2 | 2 < 4		 |  T RUN LOOP	total = 3 + a[2] = 3 + "3"
	# 3 | 3 < 4		 |  T RUN LOOP  total = 6 + a[3] = 6 + "4" = 10
	# 4 | 4 < 4		 |  F EXIT LOOP

'''
This function takes a single positive integer parameter and returns
the sum of the digits
Parameters: i >= 0
return: returns sum of the digits

preondition: i is a valid integer greater than 0
'''
def sumDigitsA(a):

	total = 0

	while (a > 0):
		total = total + a % 10 #access the ones digit
		a = a // 10

	#Trace
	# a = 57
	#
	#  a |  a > 0 |
	# 57 |  57> 0 | TRUE RUN LOOP total = 0 + 7, a = 5
	# 5  |  5 > 0 | TRUE RUN LOOP total = 7 + 5, a = 0
	# 0  |  0 > 0 | FALSE EXIT LOOP

	return total

print(sumDigitsA(57))




'''
#Test Code for missing_char

print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))
'''

'''
#Test Code for isEven

print(isEven(0))
print(isEven(10))
print(isEven(9))

for i in range(0, 100, 1):
	print(str(i)+" is "+str(isEven(i)))
'''
