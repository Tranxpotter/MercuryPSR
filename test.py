import pyautogui
import keyboard
import time



def move():
    pyautogui.mouseDown()
    pyautogui.drag(-100, 0, 1)
    pyautogui.drag(94, 0, 1)
    pyautogui.drag(0, 100, 1)
    pyautogui.drag(0, -99, 1)
    pyautogui.mouseUp()
    

keyboard.add_hotkey("space", move)

while True:
    pass

