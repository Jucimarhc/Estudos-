import os
import time

nome = []
idade = []
salario = []
sexo = []
e_civil = []

def menu():
  print('=' * 5, 'CRUD', '=' * 5)
  print('Bem Vindo!')
  print('[1] Adicionar\n[2] Ler\n[3] Atualizar\n[4] Deletar\n[5] Sair')
  
def cabecalho():
  print('=' * 5, 'CADASTRO', '=' * 5)

def f_nome():
  cabecalho()
  n = input('Digite seu nome: ')
  while len(n) <= 3:
    n = input('Precisa ter mais que 3 digitos. \nDigite novamente: ')
  else:
    time.sleep(1)
    nome.append(n)
    os.system('clear')


def f_idade():
  cabecalho()
  def f_tentativa_idade():
    try:
      os.system('clear')
      cabecalho()
      i = int(input('Digite sua idade: '))
      if (i <= 0) or (i > 150):
        os.system('clear')
        cabecalho()
        print('Idade invalida.')
        time.sleep(1)
        f_tentativa_idade()
      else:
        time.sleep(1)
        print(i)
        idade.append(i)
        os.system('clear')
        return i
    except ValueError:
      print('Por gentileza, digite uma idade.')
      time.sleep(2)
      f_tentativa_idade()
  f_tentativa_idade()

  

def f_salario():
  cabecalho()
  s = int(input('Digite o seu salário: '))
  while s <= 0:
    s = int(input('Seu salário tem que ser acima de 0 R$: '))
  else:
    time.sleep(1)
    salario.append(s)
    os.system('clear')

def f_sexo():
  cabecalho()
  sex = input('- masculino\n- feminino\n- indefinido\n\nDigite o sexo: ')
  while (sex != 'masculino') and (sex != 'feminino') and (sex != 'indefinido'):
    sex = input('Erro. Digite novamente o seu sexo: ')
  else:
    time.sleep(1)
    sexo.append(sex)
    os.system('clear')
  
  
    
def f_e_civil():
  cabecalho()
  e_civ = input('- solteiro\n- casado\n- viuvo\n\nDigite o estado civil: ')
  while (e_civ != 'solteiro') and (e_civ != 'casado') and (e_civ != 'viuvo'):
    e_civ = input('Digite novamente: ')
  else:
    time.sleep(1)
    e_civil.append(e_civ)
    os.system('clear')

def f_add():
  os.system('clear')
  while True:
    f_nome()
    f_idade()
    f_salario()
    f_sexo()
    f_e_civil()
    cabecalho()
    print('Sim [1]\nNão [2]')
    fim_add = int(input('Deseja continuar? '))
    if fim_add == 2:
      os.system('clear')
      break
    else:
      os.system('clear')
      continue
  



def f_ler_nao_cadastrado():
  os.system('clear')
  print('=' * 5, 'Leitura', '=' * 5)
  print('Nome não cadastrado.\n')


while True:
  os.system('clear')
  print(nome, idade, salario, sexo, e_civil)
  valor_menu = 0 #Variavel Menu
  menu()
  valor_menu = int(input('Escolha a opção: '))      
  
  if valor_menu == 1:
    f_add()
  
  
  
  
  elif valor_menu == 2:
    os.system('clear')
    while valor_menu == 2:
      print('=' * 5, 'Leitura', '=' * 5)
      ler_nome = input('Escreva um nome: ')
      for i in nome:
        if ler_nome == i:
          aux = nome.index(ler_nome)
          print(' nome: ', nome[aux],'\n','idade: ', idade[aux],'\n', 'salario: ', salario[aux],'\n', 'sexo: ', sexo[aux],'\n', 'estado civil: ', e_civil[aux])
          time.sleep(3)
          os.system('clear')
          print('=' * 5, 'Leitura', '=' * 5)
          buscar_1 = int(input('Deseja procurar novamente? \nSim [1]\nNão [2]\nEscolha uma opção: '))
          if buscar_1 == 2:
            break
          else:
            os.system('clear')
            continue
          break
      else:
        f_ler_nao_cadastrado()
        buscar_2 = int(input('Deseja procurar novamente? \nSim [1]\nNão [2]\nEscolha uma opção: '))
        if buscar_2 == 2:
          break
        else:
          os.system('clear')
          continue
        break
      break
  

 
  elif valor_menu == 3:
    os.system('clear')
    print('=' * 5, 'Atualizar', '=' * 5)
    ler_nome2 = input('Digite o nome para atualizar a informação: ')
    for i in nome:
      if ler_nome2 == i:
        aux2 = nome.index(ler_nome2)
        print(' nome: ', nome[aux2],'\n','idade: ', idade[aux2],'\n', 'salario: ', salario[aux2],'\n', 'sexo: ', sexo[aux2],'\n', 'estado civil: ', e_civil[aux2])
        print('======================')
        att = int(input('Qual informação deseja atualizar? \n[1] Nome\n[2] Idade\n[3] Salário\n[4] Sexo\n[5] Estado Civil\nEscolha a opção: '))
        if att == 1:
          print('======================\n')
          nome[aux2] = input('Insira o novo nome: ')
          time.sleep(1)
        elif att == 2:
          print('======================\n')
          idade[aux2] = input('Insira a idade: ')
          time.sleep(1)
        elif att == 3:
          print('======================\n')
          salario[aux2] = input('Insira salário: ')
          time.sleep(1)
        elif att == 4:
          print('======================\n')
          sexo[aux2] = input('- masculino\n- feminino\n- indefinido\n\nDigite o sexo: ')
          time.sleep(1)
        elif att == 5:
          print('======================\n')
          e_civil[aux2] = input('- solteiro\n- casado\n- viuvo\n\nDigite o estado civil: ')
          while (e_civil[aux2] != 'solteiro') or (e_civil[aux2] != 'casado'):
            e_civil[aux2] = input('Digite novamente: ')
          else:
            print(nome, idade, salario, sexo, e_civil)
            time.sleep(2)
        else:
          break

 
  elif valor_menu == 4:
    os.system('clear')
    print('=' * 5, 'Deletar', '=' * 5)
    ler_nome3 = input('Digite o nome deletar os dados: ')
    for i in nome:
      if ler_nome3 == i:
        aux3 = nome.index(ler_nome3)
        print(' nome: ', nome[aux3],'\n','idade: ', idade[aux3],'\n', 'salario: ', salario[aux3],'\n', 'sexo: ', sexo[aux3],'\n', 'estado civil: ', e_civil[aux3])
        print('======================')
        del1 = int(input('Deseja deletar? \n[1] Sim\n[2] Não\nEscolha a opção: '))
        if del1 == 1:
          print('======================\n')
          del nome[aux3], idade[aux3], salario[aux3], sexo[aux3], e_civil[aux3]
          print('Deletado.')
          time.sleep(1)
        else:
          print('======================\n')
          print('Retornando...')
          time.sleep(2)
      else:
        print('Não encontrado. Retornando...')
        time.sleep(1)
        break
  
  elif valor_menu == 5:
    os.system('clear')
    print('Obrigado por utilizar o CRUD!')
    break
# idade[nome.index(aux2)]