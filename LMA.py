from PIL import Image,ImageGrab
import pyautogui
import time

time.sleep(5)

coord = x,y = 1067,171
#print(image.getpixel(coord))
#(97, 194, 247)
#image.save("POL.jpg")
while True:
    try:

        image = ImageGrab.grab()
        if image.getpixel(coord)==(97, 194, 247):
            pyautogui.typewrite("leavemealone")
        if keyboard.is_pressed("="):
            break

    except:
        pass
