#Standard Counted Loop

# Trace Table
'''
If i = 5
i  | i < 5   | sum  
-	   -	    0
0  | 0 < 5 T |  0 + 0 = 0
1  | 1 < 5 T |  0 + 1 = 1
2  | 2 < 5 T |  1 + 2 = 3
3  | 3 < 5 T |  3 + 3 = 6
4  | 4 < 5 T |  6 + 4 = 10
5  | 5 < 5 F | EXIT LOOP

'''
sum = 0
for i in range(0, 101,1):
	if (i % 2 == 0): #checks if even
		sum = sum + i

print(sum)



sum = 0
for i in range(0, 101,2):
	sum = sum + i

#		0   1  2  3  4  5  6  7  8   9   10
data = [100,56,90,32,54,12,43,65,234,654,42]

sum = 0
for i in range(0, len(data), 1):
	sum = sum + data[i]

average = sum/len(data)
print(average)









#Standard Conditional Loops