import pyautogui
from time import sleep
import pyperclip

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey("ctrl","v")

pyautogui.moveTo(87,1059)
sleep(0.5)
pyautogui.click()
pyautogui.write("bloco")
sleep(0.5)
pyautogui.moveTo(147,516)
pyautogui.click()
sleep(0.5)
escrever_frase("Automação é incrivel!!!")
pyautogui.press("enter")