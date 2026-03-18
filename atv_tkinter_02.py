import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

#Nome da Janela
tela  = tk.Tk()
tela.title("Formulário de Cadastro")
tela.minsize(500,500)
tela.geometry("500x500")

#Subtitulo
sub_titulo = ttk.Label(tela,text="Dados Pessoais",font=("Times New Roman",10,"bold")).grid(row=0, column=1)
vazio= ttk.Label(tela,text="").grid(row=1, column=1)

#Entrada do nome
msg_nome = ttk.Label(tela,text="Insira seu Nome: ",font=("Times New Roman",10)).grid(row=2, column=0)
entrada_nome = tk.Entry(tela, width=30).grid(row=2, column=1)
vazio= ttk.Label(tela,text="").grid(row=3, column=3)

#Entrada da Idade
msg_idade = ttk.Label(tela,text="Insira sua Idade: ",font=("Times New Roman",10)).grid(row=4, column=0)
entrada_idade = tk.Entry(tela, width=30).grid(row=4, column=1)
vazio= ttk.Label(tela,text="").grid(row=5, column=5)

#Subtitulo dados Profissionais
sub_titulo_profissional = ttk.Label(tela,text="Dados Profissionais",font=("Times New Roman",10,"bold")).grid(row=6, column=1)
vazio= ttk.Label(tela,text="").grid(row=7, column=7)

#Escolaridade
escolaridade = ttk.Label(tela, text="Selecione sua escolaridade: ",font=("Times New Roman",10)).grid(row=8, column=0)
combo_escolaridade = ttk.Combobox(tela,width=28,
    values=[
        "Ensino Médio Incompleto",
        "Ensino Médio Cursado",
        "Ensino Médio Completo",
        "Ensino Superior Incompleto",
        "Ensino Superior Cursando",
        "Ensino Superior Completo"
    ]
).grid(row=8, column=1)
vazio= ttk.Label(tela,text="").grid(row=9, column=9)

#Área de Atuação
area = tk.IntVar()

tk.Label(tela, text="Selecione sua Área de Atuação: ", font=("Times New Roman",10,"bold")).grid(row=10, column=1)
tk.Radiobutton( tela, text="Técnico em Informática", font=("Times New Roman",10) ,value=1, variable=area)\
    .grid(row=11,column=1)
tk.Radiobutton(tela, text="Técnico em Enfermágem", font=("Times New Roman",10) ,value=2, variable=area)\
    .grid(row=12, column=1)
tk.Radiobutton(tela, text="Técnico em Segurança do Trabalho", font=("Times New Roman",10) ,value=3, variable=area)\
    .grid(row=13, column=1)
tk.Radiobutton(tela, text="Técnico em Estética", font=("Times New Roman",10) ,value=4, variable=area)\
    .grid(row=14, column=1)
vazio= ttk.Label(tela,text="").grid(row=15, column=15)

#Botão de Enviar
tk.Button(tela,text="Enviar Formulário").grid(row=16,column=1)

#Função de Enviar
def enviar():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    info_escola = combo_escolaridade.get()

    # Descobrir área selecionada
    if area.get() == 1:
        area_atuacao = "Técnico em Informática"
    elif area.get() == 2:
        area_atuacao = "Técnico em Enfermagem"
    elif area.get() == 3:
        area_atuacao = "Técnico em Segurança do Trabalho"
    elif area.get() == 4:
        area_atuacao = "Técnico em Estética"
    else:
        area_atuacao = "Nenhuma área selecionada"

    # Mostrar no MessageBox
    messagebox.showinfo(
        "Dados do Formulário",
        f"Nome: {nome}\n"
        f"Idade: {idade}\n"
        f"Escolaridade: {info_escola}\n"
        f"Área de Atuação: {area_atuacao}"
    )

#Botão de Enviar
tk.Button(tela, text="Enviar Formulário", command=enviar).grid(row=16, column=1)

tela.mainloop()