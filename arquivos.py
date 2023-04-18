import os

w=input("Escolha 1 para adicionar ou 2 atualiza")
import os
from posixpath import split

if w == 1:
    try:
        f = open("Login_senha.txt","a")
        nome = input ("Digite seu nome:")
        senha = input("Digite sua senha:")
    except OSError as erro:
        print("erro ao criar o arquivo ")
        print("Descrição", erro)
    else:
        print("arquivo Criado")
    f.close()

if w == 2:
    userName = input("digite seu nome:")
    userPass = input ("digite sua senha:")
    f = open("Login_senha.txt")

    Novasenha = []

    for linha in f.readlines():
        nome = linha.strip ("\n").split(":")[0]
        senha = linha.strip("\n").split(":")[1]      
    if userName == nome:
        print(nome)  
        if userPass == senha:
            print("Senha correta", senha)  
