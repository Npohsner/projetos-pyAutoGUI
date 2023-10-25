import pyautogui
from time import sleep

for i in range(7):
    pyautogui.moveTo(1381,237, duration=0.5)
    pyautogui.dragTo(1369,902,button="left",duration=0.5)