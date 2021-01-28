import math
#https://www.nayuki.io/res/dwite-programming-contest-solutions/dwite-200410-p1.pdf
#
#
#Don't print out anything except for the required output

#Strategy - Always start off by setting your inputs if possible
#			once the problem works then setup the inputs or read from file
x1 = 2
y1 = 4
x2 = 4
y2 = 8


# ((y2-y1)^2 + (x2 - x1)^2)^(1/2)
#r = math.sqrt((y2 - y1)*(y2 - y1) + (x2 - x1)*(x2 - x1))
#Python Shortcut - ** means power in python
r = ((y2 - y1)**(2) + (x2 - x1)**(2))**(1/2)

a = 3.14159*r**2

a = round(a,3)
print(a)


