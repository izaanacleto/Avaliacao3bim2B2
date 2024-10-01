import time  

emails_cadastrados = []
senhas_cadastradas = []

def validar_email(email):
    return "@" in email and "." in email


def validar_senha(senha):
    tem_letra = False
    tem_numero = False
    tem_especial = False

    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
        if caractere.isalpha():
            tem_letra = True
        if not caractere.isdigit() and not caractere.isalpha():  
            
            tem_especial = True

    return len(senha) >= 8 and tem_letra and tem_numero and tem_especial

tentativas = 0  

while True:
    if tentativas >= 3:  
        print("Número máximo de tentativas atingido. Tente novamente após 5 segundos!")

        print("Aguarde 5 segundos...")
        time.sleep(1)
        print("Aguarde 4 segundos...")
        time.sleep(1)
        print("Aguarde 3 segundos...")
        time.sleep(1)
        print("Aguarde 2 segundos...")
        time.sleep(1)
        print("Aguarde 1 segundo...")
        time.sleep(1)

        tentativas = 0 
        
    email = input("Digite seu e-mail: ")

    if email in emails_cadastrados:
        print(f"E-mail {email} já cadastrado!")
        continue 

    senha = input("Crie uma senha: ")

    if validar_email(email):
        if validar_senha(senha):
            senha_confirmacao = input("Confirme sua senha: ")

            if senha == senha_confirmacao:
                print(f"Login e senha cadastrados com sucesso! E-mail: {email}")
                emails_cadastrados.append(email)
                senhas_cadastradas.append(senha)
               
            else:
                print("As senhas não coincidem. Tente novamente.")
                tentativas = tentativas + 1  
        else:
            print("Senha inválida. A senha deve ter pelo menos 8 caracteres, contendo letras, números e caracteres especiais.")
            tentativas = tentativas + 1  
    else:
        print("E-mail inválido. O e-mail deve ter '@' e '.'")
        tentativas = tentativas + 1  