import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()

janela.title("Formulário de Login")
janela.minsize(200,200)
janela.maxsize(500,500)
janela.configure(background="#71c9fc")
janela.geometry("450x380")

#Nome do Formulário
usuario = ttk.Label(janela, text="Formulário de Login",background="#71c9fc", font=("Arial", 18,"bold"))
usuario.place(x=110,y=21.2)

#Registro do Usuário
usuario = ttk.Label(janela, text="Usuário",background="#71c9fc", font=("Arial", 17,"bold"))
usuario.place(x=65,y=100)
entrada_usuario = tk.Entry(janela, width=10,font=("Arial",18))
entrada_usuario.place(x=41.6,y=130)

#Registro da Senha
senha = ttk.Label(janela, text="Senha",background="#71c9fc", font=("Arial", 17,"bold"))
senha.place(x=70,y=180)
entrada_senha = tk.Entry(janela, width=10,font=("Arial",18))
entrada_senha.place(x=41.6,y=210)

#Foto do Gato
imagem = tk.PhotoImage(file="Gato.png")
imagem = imagem.subsample(3,3)
tk.Label(janela, image=imagem,background="#71c9fc").place(x=220,y=110)

#Botão
def clicar():
    messagebox.showinfo("Mensagem: ","Usuário Logado Com Sucesso!")
botao = tk.Button(janela, text="Enviar Formulário", font=("arial",13,"bold"),command=clicar)
botao.place(x=30,y=270)



janela.mainloop()