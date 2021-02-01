class Fraction:
#A class is a blueprint to make a object
#Objects have attributes (fields/variables) and behaviours (methods)

	#constructor
	def __init__(self, n, d):
		self.num = n
		self.den = d


	def addFractions(f1, f2):

		fresult = new Fraction(f1num*f2den + f2num*f1den,f1den*f2den)

	def printFraction():
		print(str(self.num)+"/"+str(self.den))




#Write a program that takes two fractions and adds them


#With a class
#Creating a Fraction object and setting f1.num to 5 and f1.den to 6
f1 = Fraction(5,6)
#Creating a Fraction object and setting f2.num
f2 = Fraction(3,8)

#self if the implied object - it is refering to the object that called the method

f1.printFraction()
f2.printFraction()

word = "monkey"
school = "UCC"

word.upper()
school.upper()
"alan".upper()





