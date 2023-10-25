import pyautogui
from time import sleep

pyautogui.moveTo(91,1060)
pyautogui.click()
pyautogui.write("chrome")
pyautogui.moveTo(144,512)
sleep(0.5)
pyautogui.click()
sleep(3)
pyautogui.write("wikipedia Brasil")
sleep(0.5)
pyautogui.press("enter")
sleep(1)
pyautogui.moveTo(1082,357)
sleep(0.5)
pyautogui.click()
sleep(1)
pyautogui.scroll(-2200)
