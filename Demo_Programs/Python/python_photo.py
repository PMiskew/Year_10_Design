from tkinter import *
import webbrowser

def callback(event):
    webbrowser.open_new(r"http://www.your-image.com")

root = Tk()
link = Label(root, text="The image", fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", callback)
root.mainloop()