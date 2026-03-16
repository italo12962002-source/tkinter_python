import tkinter as tk

janela_main = tk.Tk()

janela_main.title("Sylveon")
janela_main.configure(background="#f19caf")
janela_main.minsize(200,200)
janela_main.maxsize(700,700)
janela_main.geometry("500x500")


tk.Label(janela_main,
         text="Sylveon",
         bg="#b6e5f9",
         font=("Arial",20,"bold")
         ).pack()

imagem = tk.PhotoImage(file="sylvion_p.png")
imagem = imagem.subsample(3,3)
tk.Label(janela_main, image=imagem).pack()

tk.Label(janela_main,
         text="Sylveon, o Pokemon Entrelaçamento.\n O Sylveon é do tipo fada, evolui após\n um certo nível de amizade do seu Eevee",
         bg="#b6e5f9",
         font=("Arial",20,"")
         ).pack()

janela_main.mainloop()