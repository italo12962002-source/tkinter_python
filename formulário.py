import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
#Nome da Janela
janela  = tk.Tk()
janela.title("Formulário")

#Entrada do Nome
label_entrada = ttk.Label(janela,text="Nome: ")
label_entrada.pack()
entrada = tk.Entry(janela)
entrada.pack()

#Opções de Sexo
label_sexo =ttk.Label(janela, text="Selelecione o seu sexo: ")
label_sexo.pack()
opcao = tk.IntVar()


opc1 = tk.Radiobutton(janela, text="Masculino", variable=opcao, value=1)
opc2 = tk.Radiobutton(janela, text="Feminino", variable=opcao, value=2)
opc3 = tk.Radiobutton(janela, text="Outro", variable=opcao, value=3)

opc1.pack()
opc2.pack()
opc3.pack()

label_entrada_outro = ttk.Label(janela,text="Se outro, qual? ")
label_entrada_outro.pack()
entrada1 = tk.Entry(janela)
entrada1.pack()

#Listbox
lista = tk.Listbox(janela)
label_pecados = ttk.Label(janela, text="Selecione um dos sete pecados Capitais: ")
label_pecados.pack()
lista.insert(1, "Ira")
lista.insert(2, "Gula")
lista.insert(3, "Preguiça")
lista.insert(4, "Orgulho")
lista.insert(5, "Luxuria")
lista.insert(6, "Inveja")
lista.insert(7, "Ganância")
lista.pack()

#Combobox
label_combo = ttk.Label(janela, text="Selecione o estado: ")
label_combo.pack()
combo =ttk.Combobox(janela, values=["MG","RJ","RS","RN","CE"])
combo.pack()

#Termos e Condições
checkbox = tk.IntVar()
check = tk.Checkbutton(janela, text="Aceito os Termos e Condições", variable=checkbox)
check.pack()

#Botão
def clicar():
    messagebox.showinfo("Mensagem: ","Formulário enviado com sucesso!")
btn = tk.Button(janela, text="Enviar Formulário", command=clicar)
btn.pack()

janela.mainloop()