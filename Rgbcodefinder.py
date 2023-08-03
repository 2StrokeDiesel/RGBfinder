import pyautogui
import time
while True:
    x, y = pyautogui.position()
    r,g,b = pyautogui.pixel(x, y)
    print(r,g,b)
    time.sleep(0.1)
