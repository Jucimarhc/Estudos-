
""" f = open("bashrc","a")
f.write("\n primeira aula de phyton ")
f.close()


f= open("bashrc")
arquivo = f.read()
print(arquivo) """


"""nome = input("Digite seu Login:")
senha = input("Digite sua senha :")
f = open("Login é senha.txt,","a") 
f.write ("Login :{}\n".format(nome) + "Senha:{}\n".format(senha))
f.close()
print("Nome e senha do usuário foram salvos no arquivo.")"""
 
import os

try :
    f = open("Login_senha.txt","a")
    nome = input ("Digite seu nome:")
    senha = input("Digite sua senha:")
except OSError as erro:
    print("erro ao criar o arquivo ")
    print("Descrição", erro)
else:
    print("arquivo Criado") 

Novasenha = []

for linha in f.readlines():
    nome = linha.strip ("\n").split(":")[0]
    senha = linha.strip("\n").split(":")[1]      
    if userName == nome:
      print(nome)  
    if userPass == senha:
        print("Senha correta", senha)  

try:
    os.mkdir('Login')
except FileExistsError as erro:
    print("Diretorio ja existe \n", erro)
except PermissionError as erro: 
    print("Vocé não possue privilegios")
    print("Descrição",erro)    
    
try:
    os.replace("Login_senha.txt","Login/Login_senha.txt")
except FileNotFoundError as erro:
    print("Arquivo não Existe\n")
    print("Descrição", erro)
