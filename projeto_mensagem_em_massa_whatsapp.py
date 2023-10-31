import pyautogui
import webbrowser   

from time import sleep


# Exitem duas maneiras: Digitando uma lista

telefones = [551199999999, 5511988888888]

# Importando um arquivo txt. com uma lista

telefones = []

with open("fones.txt","r") as arquivo:
   for linha in arquivo:
      telefones.append(linha.split("\n")[0])
      

for telefone in telefones:
   webbrowser.open_new(f"https://api.whatsapp.com/send?phone={telefone}") 
   sleep(10)
   pyautogui.click(1132,726,duration=1)
   sleep(5)
   pyautogui.typewrite("Teste para um bot que estou criando que passa mensagem em massa para o WhatsApp, bjo.")
   sleep(5)
   pyautogui.press("enter")
   sleep(60)


