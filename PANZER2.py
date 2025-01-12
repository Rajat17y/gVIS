import pyautogui
import keyboard

while True:
    if keyboard.is_pressed("="):
        while True:
            if keyboard.is_pressed("-"):
                break
            else:
                pyautogui.typewrite("panzer")
    if keyboard.is_pressed("h"):
        break
    
