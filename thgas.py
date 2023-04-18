# 4 linhas
import tkinter as tk #Importando a GUI tkinter que vai ser chamada usando "tk"
from PIL import Image, ImageTk #Biblioteca de processamento de imagem, para depois serem usadas no Tk
from tkinter import messagebox #Importando o messagebox
import sys
# 37 linhas
def login():
    global tela_login, usuario_verify, senha_verify, entrada_usuario, entrada_senha, wallpaper_login, label4

    # Criação da janela de login
    tela_login = tk.Toplevel(tela)
    tela_login.title("Login")
    tela_login.geometry("400x300+500+200")
    tela_login.resizable(False, False)

    # Carregamento e redimensionamento da imagem de fundo
    fundo_login = Image.open(r"C:\Users\Felipe\Desktop\Trabalho de Python\imagens\login.jpg")
    fundo_login = fundo_login.resize((400, 300), Image.LANCZOS)
    wallpaper_login = ImageTk.PhotoImage(fundo_login)

    # Criação do label para a imagem de fundo
    label4 = tk.Label(tela_login, image=wallpaper_login)
    label4.place(x=0, y=0, relwidth=1, relheight=1)
    label4.bind('<Configure>', attframewallpaper_login)

    # Criação das variáveis de verificação do usuário e senha
    usuario_verify = tk.StringVar()
    senha_verify = tk.StringVar()

    # Criação dos widgets de entrada de usuário e senha e do botão de login
    label2 = tk.Label(tela_login, text="Usuário", bg="White")
    label2.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    entrada_usuario = tk.Entry(tela_login, textvariable=usuario_verify)
    entrada_usuario.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    label3 = tk.Label(tela_login, text="Senha", bg="White")
    label3.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    entrada_senha = tk.Entry(tela_login, textvariable=senha_verify, show='*')
    entrada_senha.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    botao1 = tk.Button(tela_login, text="Login", width=10, height=1, command=verificar)
    botao1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    # Configuração do comportamento do botão fechar da janela de login
    tela_login.protocol("WM_DELETE_WINDOW", fechar)
# 14 linhas
def attframewallpaper_login(event):
    global wallpaper_login, label4
    
    # obtém a nova largura e altura da janela
    largura = event.width
    altura = event.height
    
    # redimensiona a imagem de fundo
    fundo_login = Image.open(r"C:\Users\Felipe\Desktop\Trabalho de Python\imagens\login.jpg")
    fundo_login = fundo_login.resize((largura, altura), Image.LANCZOS)
    wallpaper_login = ImageTk.PhotoImage(fundo_login)
    
    # atualiza a imagem do label
    label4.configure(image=wallpaper_login)
# 10 linhas
def verificar():
    if usuario_verify.get() == "admin" and senha_verify.get() == "123":
        print("Acesso Libero")
        tela_login.destroy()
        tela.deiconify()
    else:
        print("Acesso Negado")
        messagebox.showerror("Erro","Usuário ou senha Inválidos")
        entrada_usuario.delete(0,'end')
        entrada_senha.delete(0,'end')
# 3 linhas
def fechar():
    tela_login.destroy()
    sys.exit()
# 12 linhas
def criar_tela():
    global tela, wallpaper
    tela = tk.Tk() #Criando a janela Tkinter usando o construtor toolkit tkinter
    tela.geometry("800x600") #Aqui eu defino o width e height da janela, e o posicionamento inicial dela
    tela.resizable(False,False) #tornar False o redimensionamento da janela, tanto width quanto heigth 
    tela.title("RAD") #Titulo da aplicação
    fundo = Image.open(r"C:\Users\Felipe\Desktop\Trabalho de Python\imagens\sound_2-wallpaper-1366x768.jpg") #abrindo a imagem
    fundo = fundo.resize((800,600), Image.LANCZOS) #Redimensionando a imagem
    wallpaper = ImageTk.PhotoImage(fundo) #Objeto Photoimage sendo criado e recebendo a imagem preparada "fundo", esse objeto é atribuido à variavel wallpaper
    label0 = tk.Label(tela, image=wallpaper) #É aqui que eu carrego a imagem na interface, estou criando um objeto label e atribuindo uma imagem como segundo argumento, o primeiro argumento é a 'tela' que é onde o label vai ser adicionado, tudo isso sendo atribuido à variavel label0
    label0.pack() #isso aqui posiciona o label0 no centro da tela
    #tela.withdraw()
# 7 linhas
def verificar_igual():
    if igualsenha1.get() == igualsenha2.get():
        print("Sucesso")
        tela_adicionar.destroy()
    else:
        tela_adicionar.attributes('-topmost', True)
        messagebox.showerror("Erro","Verifique a senha criada", parent=tela_adicionar)
# 2 linhas
def fechar_adicionar():
    tela_adicionar.destroy()
# 33 linhas
def criar_menu():
    # Vamo criar a barra de menu
    menubar = tk.Menu(tela) # Menu criado, atribuido à variavel menubar
    arquivo_menu = tk.Menu(menubar,tearoff=0) # arquivo_menu recebe o objeto menu,(menubar)/tearoff= Para que o usuario não separe o menu da janela
    editar_menu = tk.Menu(menubar,tearoff=0)
    ferramentas_menu = tk.Menu(menubar,tearoff=0)
    opcoes_menu = tk.Menu(menubar,tearoff=0)
    sobre_menu = tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Arquivo", menu=arquivo_menu) # O método add_cascade() é usado para adicionar um item de menu que abre um submenu
    menubar.add_cascade(label="Editar", menu=editar_menu) # Aqui eu estou criando varias opçoes na barra de menu
    menubar.add_cascade(label="Ferramentas", menu=ferramentas_menu) # Label argumento serve para colocar o texto na opção da menu bar
    menubar.add_cascade(label="Opções", menu=opcoes_menu) # O segundo argumento menu=arquivo_menu seleciona o menu que ta relacionado ao objeto
    menubar.add_cascade(label="Sobre", menu=sobre_menu) # tk.menu
    tela.config(menu=menubar) # Aqui a menubar esta sendo configurada, sendo associada à barra de menu da janela principal (tela) desse modo aparecendo no topo da janela principal (tela) permitindo que o menu seja acessado de qualquer tela da aplicação 
    arquivo_menu.add_command(label="Novo  Ctrl+Shift+N")
    arquivo_menu.add_command(label="Abrir  Ctrl+O")
    arquivo_menu.add_command(label="Salvar  Ctrl+S")
    editar_menu.add_command(label="Atualizar  Ctrl+F5")
    editar_menu.add_command(label="Copiar  Ctrl+C")
    editar_menu.add_command(label="Colar  Ctrl+V")
    editar_menu.add_command(label="Cortar  Ctrl+X")
    editar_menu.add_command(label="Pesquisar  Ctrl+F")
    sobre_menu.add_command(label="Creditos")
    sobre_menu.add_command(label="Versão")
    opcoes_menu.add_command(label="Idioma")
    opcoes_menu.add_command(label="Config")
    opcoes_menu.add_command(label="Config")
    opcoes_menu.add_command(label="Config")
    ferramentas_menu.add_command(label="Adicionar", command=adicionar_tela)
    ferramentas_menu.add_command(label="Visualizar")
    ferramentas_menu.add_command(label="Remover")
    ferramentas_menu.add_command(label="Buscar")
    ferramentas_menu.add_command(label="Filtrar")
# 29 linhas
def adicionar_tela():
    global tela_adicionar, label5, igualsenha1, igualsenha2, botao2, botao3
    tela_adicionar = tk.Toplevel(tela)
    tela_adicionar.overrideredirect(True)
    tela_adicionar.title("Adicionando Usuário")
    tela_adicionar.geometry("400x300+500+200")
    tela_adicionar.resizable(False,False)

    igualsenha1 = tk.StringVar()
    igualsenha2 = tk.StringVar()

    label5 = tk.Label(tela_adicionar, text="Usuário")
    label5.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    entrada_usuario1 = tk.Entry(tela_adicionar)
    entrada_usuario1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    label6 = tk.Label(tela_adicionar, text="Senha")
    label6.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    entrada_senha1 = tk.Entry(tela_adicionar, textvariable=igualsenha1)
    entrada_senha1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    label7 = tk.Label(tela_adicionar, text="Confirmar Senha")
    label7.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    entrada_confirmar = tk.Entry(tela_adicionar, textvariable=igualsenha2)
    entrada_confirmar.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    botao2 = tk.Button(tela_adicionar, text="Salvar", width=10, height=1, command=verificar_igual, bg="#80ff80", activebackground="#b3ffb3")
    botao2.place(relx=0.2, rely=0.8)
    botao3 = tk.Button(tela_adicionar, text="Cancelar", width=10, height=1, command=fechar_adicionar, bg="#ff3333", activebackground="#ff6666")
    botao3.place(relx=0.6, rely=0.8)

    tela_adicionar.lift()

criar_tela()
tela.withdraw()
login()
criar_menu()
tela.mainloop() #Chama a tela principal