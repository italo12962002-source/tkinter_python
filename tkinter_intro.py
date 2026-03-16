import tkinter as tk

janela_main = tk.Tk()

janela_main.title("Jan é lá")
janela_main.configure(background="#ffc2e8")
janela_main.minsize(200,200)
janela_main.maxsize(500,500)
janela_main.geometry("300x300")


tk.Label(janela_main,
         text="Hello Kitty",
         bg="#ffc2e8",
         font=("Arial",20,"bold")
         ).pack()
tk.Label(janela_main,
         text="Italo samuel",
         bg="#ffc2e8",
         font=("Arial",20)
         ).pack()

imagem = tk.PhotoImage(file="hellokitty.png")
imagem = imagem.subsample(3,3)
tk.Label(janela_main, image=imagem).pack()


janela_main.mainloop()