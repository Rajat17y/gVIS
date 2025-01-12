from PIL import Image,ImageGrab
import pyautogui
import time
import keyboard
import speech_recognition as sr



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
                if keyboard.is_pressed("ctrl+f"):
                    print("voice activated")
                    r = sr.Recognizer()
                    with sr.AudioSource(device_index = 1) as source:
                        audio = r.listen(source)
                        try:
                            text = r.recognize_google(audio)
                            if (text=="Panzer" or text=="panzer"):
                                pyautogui.typewrite("panzer")
                                print("panzer")
                        except:
                            pass
                if keyboard.is_pressed('-'):
                    print(tim_Arm)
                    print(tim_Heal)
                    break
                        
                
        except:
                pass
       

input()




