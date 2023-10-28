import pyautogui
import webbrowser
import keyboard
from time import sleep



# Entrar no site
webbrowser.open_new("https://guitarflash.com/?lg.pt")
sleep(3)
# Slecionar jogo
pyautogui.click(1212,406,duration=0.5)
sleep(5)
pyautogui.click(1623,752,duration=0.5)
sleep(5)
pyautogui.click(1256,901,duration=0.5)
sleep(5)
pyautogui.scroll(-300)
sleep(5)
pyautogui.press("space")
sleep(2)
while keyboard.is_pressed("1") == False:
    if pyautogui.pixelMatchesColor(1249,759,(0,152,0)):
        pyautogui.press("a")
        sleep(0.1)
    if pyautogui.pixelMatchesColor(1339,759,(255,0,0)):
        pyautogui.press("s")
        sleep(0.1)
    if pyautogui.pixelMatchesColor(1426,761,(244,244,2)):
        pyautogui.press("j")
        sleep(0.1)
