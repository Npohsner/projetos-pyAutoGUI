import pyautogui

# Alertando o usuario

pyautogui.alert(text="Iniciando sua Automação",title="Alerta",button="ok")


# Pegando informação com usuario

email = pyautogui.prompt(text="Digite seu e-mail")
print(f"Você digitou {email}")

# Fazendo confirmação como o usuario

resposta = pyautogui.confirm(text="Devemos continuar nossa automação ?",title="Confirmação",buttons=["sim","não","cancelar"])
if resposta == "sim":
    print("Continuando Automação...")
elif resposta == "não":
    print("Encerrando Automação...")
else: 
    print("Operação Cancelada")

# Fazendo senha ao ser digitada, aparecer "*"

senha = pyautogui.password(text="Digite sua senha",title="Infornações de login",mask="*")
print(senha)