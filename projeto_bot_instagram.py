import webbrowser
import pyautogui
from time import sleep

def logout():
   pyautogui.click(1875,144,duration=0.5)
   sleep(2)
   pyautogui.click(996,638,duration=0.5)
   sleep(2)
   pyautogui.click(1799,167,duration=0.5)
   sleep(2) 
   pyautogui.click(1430,682,duration=0.5)
   sleep(2) 
while True:
    # entrar no site
    webbrowser.open_new("https://instagram.com")
    sleep(3)
    # fazer login
    pyautogui.click(1518,376,duration=0.5)
    pyautogui.typewrite("login")
    sleep(0.5)
    pyautogui.click(1520,419,duration=0.5)
    pyautogui.typewrite("senha")
    sleep(0.5)
    pyautogui.click(1630,469,duration=0.5)
    sleep(3)
    # fechar alertas
    pyautogui.click(1703,346,duration=0.5)
    sleep(3)
    pyautogui.click(1464,621,duration=0.5)
    sleep(3)
    # pesquisar pagina
    pyautogui.click(996,299,duration=0.5)
    sleep(2)
    pyautogui.click(1069,229,duration=0.5)
    sleep(1)
    pyautogui.typewrite("Quem pesquisar")
    sleep(1)
    pyautogui.click(1142,296,duration=0.5)
    sleep(3)
    # ultima postagem
    pyautogui.click(1190,835,duration=0.5)
    sleep(3)
    # curtir, ou esperar 24hs
    curtiu = pyautogui.locateOnScreen("curtiu.png")
    sleep(1)
    if curtiu is not None:
        logout()
        sleep(86400)
    elif curtiu == None:
        pyautogui.click(1460,706,duration=0.5)
        sleep(3)
    # comentar foto se não tiver curtido
        pyautogui.click(1502,708,duration=0.5)
        sleep(2)
        pyautogui.typewrite("Amo muito!!!!")
        sleep(2)
        pyautogui.press("enter")
        sleep(1)
    # sair da conta
        logout()
    # pausar por 24hs
        sleep(86400)


