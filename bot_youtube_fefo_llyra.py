import pyautogui
from time import sleep

pyautogui.moveTo(87,1059)
sleep(0.5)
pyautogui.click()
pyautogui.write("chrome")
pyautogui.moveTo(128,519)
sleep(0.5)
pyautogui.click()
sleep(0.5)
pyautogui.write("www.youtube.com")
pyautogui.press("enter")
sleep(3)
pyautogui.moveTo(1246,142)
pyautogui.click()
pyautogui.write("fefo llyra")
pyautogui.press("enter")
sleep(3)
pyautogui.moveTo(1227,484)
for i in range(1):
    pyautogui.click()
    sleep(0.5)