import pyautogui
import time
x=5
while x==5:
    time.sleep(2)
    pyautogui.typewrite('This is an automated message', interval=0.05)
    pyautogui.typewrite(['enter'])
