import tkinter as tk
'''
helper
 
 0 : intger -1 don't record, 1 record

'''

recordPoints = open("recordPoints","w")

helper = [-1]

def mouseListener(e):
	#print("Moving")
	#print(e.x,":",e.y)

	if (helper[0] == 1):
		print("recording")
		recordPoints.write(str(e.x)+","+str(e.y))
	

def mouseClickB(e):

	helper[0] = helper[0]*-1



def mouseClick(e):



	print("CLIKCED")

	#logic for head
	'''
	HEAD
	61,3
	94,43
	'''
	x = e.x
	y = e.y

	if (61 < x < 94 and 3 < y < 43):
		print("HEAD")
		#logic
	



root = tk.Tk()

# create the canvas, size in pixels
canvas = tk.Canvas(root, width=155, height= 310, bg='black')

# pack the canvas into a frame/form
canvas.pack(expand=tk.YES, fill=tk.BOTH)

# load the .gif image file
gif1 = tk.PhotoImage(file='download.png')

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(0, 0, image=gif1, anchor=tk.NW)

canvas.create_polygon(70,4270,4170,4070,3969,3969,3869,3769,3669,3569,3469,3369,3268,3268,3168,3068,2967,2967,2867,2766,2766,2666,2566,2466,2366,2266,2167,2167,2067,1967,1867,1767,1667,1567,1467,1367,1267,1168,1169,1170,1071,1071,972,972,873,774,775,776,777,777,678,679,680,681,682,683,684,685,685,786,787,787,887,988,988,1088,1189,1189,1290,1290,1390,1490,1590,1691,1691,1791,1892,1892,1993,1993,2093,2193,2292,2292,2392,2491,2491,2591,2690,2691,2692,2693,2693,2593,2692,2692,2791,2791,2891,2990,2990,3090,3189,3189,3288,3388,3488,3588,3688,3788,3888,3989,4089,4189,4290,4290,4390,4491,4591,4691,4591,4491)

canvas.bind("<Motion>",mouseListener)
canvas.bind("<Button-1>",mouseClickB)

root.mainloop()

recordPoints.close()
