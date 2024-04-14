import pandas as pd
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime


class Application():
    def __init__(self): 
        self.root = Tk()
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
        self.nome_responsavel = ""  # Variável para armazenar o nome do responsável
        self.tipo_leitura = ""  # Variável para armazenar o tipo de leitura (Entrada/Saída)
        self.codigo_barras = ""  # Variável para armazenar o código de barras

        # Lendo a planilha Excel
        try:
            dados = pd.read_excel("acompanhamento.xlsx")
            df = pd.read_excel("timescan.xlsx")
            self.colaboradores = df
            self.dados=dados
            # print(self.dados)
        except Exception as e:
            print("Erro ao ler a planilha Excel:", e)
            # Se houver um erro ao ler a planilha, você pode definir um DataFrame vazio como padrão
            self.colaboradores = pd.DataFrame()
            print(pd.DataFrame())

        self.root.mainloop()  

    def tela(self):
        self.root.title("Cadastro de Clientes") 
        self.root.configure(background='white')
        self.root.configure(highlightbackground="black", highlightthickness=2)
        self.root.geometry("800x600")    
        self.root.resizable(False, False)

    def frames_da_tela(self):
        # Dados do Frame referente a Logo
        self.frame_1 = Frame(self.root, highlightbackground="black", highlightthickness=1)
        self.frame_1.place(relx=0.38, rely=0.02, relwidth=0.3, relheight=0.1)

        # Carrega a imagem da logo
        img_logo = Image.open("logo.png")
        img_logo = img_logo.resize((150, 150))  # Ajusta o tamanho da imagem conforme necessário
        logo = ImageTk.PhotoImage(img_logo)
        label_logo = Label(self.frame_1, image=logo)
        label_logo.image = logo  
        label_logo.pack(expand=True, fill='both', padx=10, pady=10)

        # Dados do Frame referente ao Nome do Responsável
        self.frame_2=Frame(self.root, highlightbackground="black", highlightthickness=1)
        self.frame_2.place(relx=0.2, rely=0.15, relwidth = 0.65, relheight=0.10)
        self.codigo_entry = Entry(self.frame_2, highlightbackground="black", highlightthickness=1)
        self.codigo_entry.place(relx=0.5, rely=0.20, relwidth = 0.4, relheight=0.6)
        label =Label(self.frame_2, text="Insira o nome do Responsável:", highlightbackground="black", highlightthickness=1)
        label.place(relx=0.05, rely=0.25, relwidth=0.4, relheight=0.5)

        # Dados Referentes ao Frame Tipo de Leitura e seus respectivos botões
        self.frame_3=Frame(self.root, highlightbackground="black", highlightthickness=1)
        self.frame_3.place(relx=0.2, rely=0.35, relwidth = 0.65, relheight=0.10)
        label =Label(self.frame_3, text="Tipo de Leitura: ")
        label.place(relx=0.05, rely=0.25, relwidth=0.4, relheight=0.5)
        button_entrada = Button(self.frame_3, text="Entrada", command=self.definir_entrada)
        button_entrada.place(relx=0.5, rely=0.25, relwidth=0.2, relheight=0.5)
        button_saida = Button(self.frame_3, text="Saída", command=self.definir_saida)
        button_saida.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.5)

        # Dados Referentes ao Frame do tipo Dados de Leitura, local onde ficarão os dados do código de barras
        self.frame_4=Frame(self.root, highlightbackground="black", highlightthickness=1)
        self.frame_4.place(relx=0.1, rely=0.50, relwidth = 0.8, relheight=0.25)
        self.label_nome_responsavel = Label(self.frame_4, text="", font=("Helvetica", 13))
        self.label_nome_responsavel.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.15)
        self.label_codigo_barras = Label(self.frame_4, text="", font=("Helvetica", 13))
        self.label_codigo_barras.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.15)
        self.label_tipo_leitura = Label(self.frame_4, text="", font=("Helvetica", 13))
        self.label_tipo_leitura.place(relx=0.1, rely=0.60, relwidth=0.8, relheight=0.15)
        self.label_dados_colaborador = Label(self.frame_4, text="Dados do Colaborador:", font=("Helvetica", 12))
        self.label_dados_colaborador.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.15)

        # Dados Referentes ao Footer
        self.frame_5=Frame(self.root, highlightbackground="black", highlightthickness=1)
        self.frame_5.place(relx=0.05, rely=0.9, relwidth = 0.9, relheight=0.05)
        label =Label(self.frame_5, text="Desenvolvido Por Honson Filho")
        label.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.4)

        # Dados Referentes à Simulação do Código de barras
        self.frame_6=Frame(self.root, highlightbackground="black", highlightthickness=1)
        self.frame_6.place(relx=0.2, rely=0.25, relwidth = 0.65, relheight=0.10)
        self.codigo_entry_codb = Entry(self.frame_6, highlightbackground="black", highlightthickness=1)
        self.codigo_entry_codb.place(relx=0.5, rely=0.20, relwidth = 0.4, relheight=0.6)
        label =Label(self.frame_6, text="Insira o Número do Cód Barras", highlightbackground="black", highlightthickness=1)
        label.place(relx=0.05, rely=0.25, relwidth=0.4, relheight=0.5)

    def criando_botoes(self):
        # Botões
        button_salvar =Button(text="Salvar", command=self.salvar_nome)
        button_salvar.place(relx=0.88, rely=0.18, relwidth=0.1, relheight=0.05)
        
        self.bt_enviar=Button(text="Enviar", highlightbackground="black", highlightthickness=1, command=self.submit)
        self.bt_enviar.place(relx=0.1, rely=0.8, relwidth = 0.8, relheight=0.05)

        self.bt_upar = Button(text="Upar", command=self.verificar_codigo)
        self.bt_upar.place(relx=0.88, rely=0.28, relwidth=0.1, relheight=0.05)

    def salvar_nome(self):
        self.nome_responsavel = self.codigo_entry.get()
        self.label_nome_responsavel.config(text="Nome do Responsável: " + self.nome_responsavel)
    
    def definir_entrada(self):
        self.tipo_leitura = "Entrada"
        self.label_tipo_leitura.config(text="Tipo de Leitura: " + self.tipo_leitura)

    def definir_saida(self):
        self.tipo_leitura = "Saída"
        self.label_tipo_leitura.config(text="Tipo de Leitura: " + self.tipo_leitura)
        
    def verificar_codigo(self):
        self.codigo = self.codigo_entry_codb.get().strip()  
        linha_colaborador = self.colaboradores[self.colaboradores['codigo'].astype(str).str.strip() == self.codigo]

        if not linha_colaborador.empty:
            self.nome = linha_colaborador.iloc[0]['nome']
            self.matricula = linha_colaborador.iloc[0]['matricula']
            self.idsap = linha_colaborador.iloc[0]['idsap']
            
            self.texto = f"Dados: {self.nome}, Matrícula: {self.matricula}, ID SAP: {self.idsap}"
            self.label_dados_colaborador.config(text="Dados: " + self.texto)
            

    def submit(self):
            
            data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            try:
                # self.dados.to_excel("acompanhamento.xlsx", index=False)
                nova_linha = {'nome': self.nome, 'matricula': self.matricula, 'idsap': self.idsap, 'responsavel': self.nome_responsavel, 'data_hora':data_hora_atual, 'tipo': self.tipo_leitura, 'setor': 'Corte'}
                self.dados = self.dados._append(nova_linha, ignore_index=True)
                self.dados.to_excel("acompanhamento.xlsx", index=False)
            except KeyError:
                self.label_dados_colaborador.config(text="Dados do Colaborador: Usuário Não Identificado na Planilha")
    

Application()
