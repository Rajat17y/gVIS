from PIL import Image,ImageGrab
import pyautogui
import time
import keyboard
from tkinter import *



#keyboard.is_pressed('h'):


time.sleep(10)
#(185, 185, 185)Armor
#(255, 150, 225)Health
cordinates_A = x,y = 896,133
cordinates_B = x,y = 1047,130
tim_Arm = 0
tim_Heal = 0

while True:
        try:
                image = ImageGrab.grab()
                if image.getpixel(cordinates_A)== (185, 185, 185):
                        pyautogui.typewrite("preciousprotection")
                        tim_Arm+=1
                if image.getpixel(cordinates_B)== (255, 150, 225):
                        pyautogui.typewrite("aspirine")
                        tim_Heal+=1
                if keyboard.is_pressed('-'):
                        print(tim_Arm)
                        print(tim_Heal)
                        break
                        
                
        except:
                pass
       

input()




