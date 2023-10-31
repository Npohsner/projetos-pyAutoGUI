import pyautogui
import keyboard
import webbrowser
import win32api
import win32con
from time import sleep

pyautogui.click(1263,603)


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed("1") == False:
    if pyautogui.pixelMatchesColor(1310,273,(0,0,0)):
        pyautogui.click(1310,273)
        
    if pyautogui.pixelMatchesColor(1399,538,(0,0,0)):
        pyautogui.click(1399,538)
        
    if pyautogui.pixelMatchesColor(1471,357,(0,0,0)):
        pyautogui.click(1471,357)
       
    if pyautogui.pixelMatchesColor(1541,481,(0,0,0)):
        pyautogui.click(1541,481)
       
