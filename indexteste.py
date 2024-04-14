import tkinter as tk

class Application:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600")
        self.frames_da_tela()
        self.criando_botoes()
        self.nome_responsavel = StringVar()  # Variável para armazenar o nome do responsável
        self.tipo_leitura = StringVar()  # Variável para armazenar o tipo de leitura (Entrada/Saída)
        self.root.mainloop()

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, highlightbackground="black", highlightthickness=1)
        self.frame_1.place(relx=0.38, rely=0.02, relwidth=0.3, relheight=0.2)
        label = Label(self.frame_1, text="Logo", font=("Helvetica", 16))
        label.pack(expand=True, fill='both', padx=10, pady=10)

        self.frame_2 = Frame(self.root, highlightbackground="black", highlightthickness=1)
        self.frame_2.place(relx=0.2, rely=0.25, relwidth=0.65, relheight=0.10)
        self.codigo_entry = Entry(self.frame_2, highlightbackground="black", highlightthickness=1, textvariable=self.nome_responsavel)
        self.codigo_entry.place(relx=0.47, rely=0.25, relwidth=0.5, relheight=0.5)
        label = Label(self.frame_2, text="Insira o nome do Responsável:", highlightbackground="black", highlightthickness=1)
        label.place(relx=0.05, rely=0.25, relwidth=0.4, relheight=0.5)

        self.frame_3 = Frame(self.root, highlightbackground="black", highlightthickness=1)
        self.frame_3.place(relx=0.2, rely=0.35, relwidth=0.65, relheight=0.10)
        label =Label(self.frame_3, text="Tipo de Leitura: ")
        label.place(relx=0.05, rely=0.25, relwidth=0.4, relheight=0.5)
        button_entrada = Button(self.frame_3, text="Entrada", command=lambda: self.set_tipo_leitura("Entrada"))
        button_entrada.place(relx=0.5, rely=0.25, relwidth=0.2, relheight=0.5)
        button_saida = Button(self.frame_3, text="Saída", command=lambda: self.set_tipo_leitura("Saída"))
        button_saida.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.5)

        self.frame_4 = Frame(self.root, highlightbackground="black", highlightthickness=1)
        self.frame_4.place(relx=0.1, rely=0.50, relwidth=0.8, relheight=0.25)
        label = Label(self.frame_4, text="Dados da Leitura")
        label.place(relx=0.3, rely=0.25, relwidth=0.4, relheight=0.5)

    def criando_botoes(self):
        self.bt_enviar = Button(self.root, text="Enviar", highlightbackground="black", highlightthickness=1)
        self.bt_enviar.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.05)

    def set_tipo_leitura(self, tipo):
        self.tipo_leitura.set(tipo)

Application()
