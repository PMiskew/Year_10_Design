import tkinter as tk


def mouseListener(e):
	print("Moving")
	print(e.x,":",e.y)

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

#canvas.create_rectangle(61,3,94,43)

#canvas.bind("<Motion>",mouseListener)
canvas.bind("<Button-1>",mouseClick)



root.mainloop()
