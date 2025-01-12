from PIL import Image,ImageGrab
import time

time.sleep(10)
print("OK")

image = ImageGrab.grab()
image.save("Sample.jpg")
