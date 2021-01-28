

def calculateTime():

	val = input()

	h = val[0:2] #inclusive:exclusive h = "09"

	h = int(h) 	# 9 - when we cast a string that is an int it just changes it
				#The process of casting removes non-significant digits

	m = val[3:5]	#inclusive:exclusive

	timeOfDay = "AM" #Assuming AM

	if (12 <= h <= 23):
		timeOfDay = "PM"
		h = h - 12
	if (h == 0):
		h = 12


	print(str(h)+":"+m+" "+timeOfDay)


for i in range(0, 3,1):
	calculateTime()








