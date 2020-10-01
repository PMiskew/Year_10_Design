from tkinter import *
from PIL import Image, ImageFilter
from PIL import ImageTk
from io import *
import requests

#Use a local file
#im = Image.open( 'image.jpg' )

#Use a url
pic_url = "https://apod.nasa.gov/apod/image/2009/BennuEjecting_OsirisRex_1169.jpg"
imageLoad = requests.get(pic_url)
image = Image.open(BytesIO(imageLoad.content))
#this opens a dedicated window for the image
#im.show()

picWidth = image.size[0] // 2
picHeight = image.size[1] // 2
picSize = (picWidth, picHeight)
image.resize(picSize)
windowSize = "%dx%d" % (picWidth,picHeight)


#display the image on a GUI
root = Tk()
root.title("Display Image from URL")
root.geometry(windowSize)
renderImage = ImageTk.PhotoImage(image)
display = Label(root, image=renderImage)
display.image = renderImage
display.pack(side=TOP)

root.mainloop()