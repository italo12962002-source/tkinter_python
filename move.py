import tkinter as tk

janela = tk.Tk()
janela.minsize(300, 300)
janela.geometry("400x400")
janela.title("Mover Elementos")

texto = tk.Label(text="Nome",font=("Open Sans",14))
texto.place(x=175,y=20)


janela.mainloop()