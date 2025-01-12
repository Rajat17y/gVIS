from PIL import ImageGrab,Image
import time
time.sleep(10)

image = ImageGrab.grab()
'''
image.save("Hsample2.jpg")
'''
cordinates = x,y = 1047,130
print(image.getpixel(cordinates))

