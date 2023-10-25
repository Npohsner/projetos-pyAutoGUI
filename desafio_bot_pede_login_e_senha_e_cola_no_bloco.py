import pyautogui

login = pyautogui.prompt(text="Digite seu login",title="Informações Usuario")
print(login)

senha = pyautogui.password(text="Digite sua senha",title="Informações Usuario",mask="*")
print(senha)

pyautogui.click(1404,79,duration=1)
pyautogui.typewrite(login)
pyautogui.press("enter")
pyautogui.typewrite(senha)