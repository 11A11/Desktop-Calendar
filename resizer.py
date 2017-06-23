import PIL
from PIL import Image

basewidth = 300
img = Image.open('test.png')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((1366,hsize), PIL.Image.ANTIALIAS)
img.save('test.png') 
