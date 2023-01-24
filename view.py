# Pacotes
from tkinter import *
from tkinter import ttk, messagebox


from functions import Inserir_Materiais, Mostrar_Estoque, Materiais_Combobox, Verificar_Quantidade, Atualizar, Enderecos_Combobox

# ------------- Gerar Executável Python: pyinstaller --onefile --noconsole --windowed {Programa} 

# -------------- Cores -------------------

co1 = "#ccc"
co2 = "#069"
co3 = "#fff"
co4 = "#063970"

# -------------- Atributos Janela --------------
Home = Tk()
Home.title("Estoque Materiais")
icone = PhotoImage(file="C:/Users/lucas/Desktop/Materiais/images/parcela.png")
Home.iconphoto(False, icone)
Home.configure(bg= co1)
Home.state('zoomed')    # Preenche toda a tela


# ------------ Dividindo A janela ----------------
frame_topo = Frame(Home, width=1500, height=200,bg= co1)
frame_topo.grid(column=0, row=1)

frame_entradas = Frame(Home, width=1325, height=475, bg= co2)
frame_entradas.place(x= 20, y=200)

frame_infos_adicionar = Frame(frame_entradas, width=450, height=440, bg= co4)
frame_infos_adicionar.place(x= 20, y=20)

selecione_l = Label(frame_infos_adicionar, text="Selecione Uma Operação Acima", bg=co4, fg=co3 ,font=("Ubuntu 19 bold"))
selecione_l.place(x=25, y= 80)

#-----------------------------------------------------------

logo = PhotoImage(file="C:/Users/lucas/Desktop/Materiais/images/logo.png", width=200, height=200)    #Logo Santuario
logo_label = Label(frame_topo, image= logo, bg= co1)
logo_label.place(x= 0, y= -20)

titulo = Label(frame_topo, text="Estoque de Materiais", bg=co1, font=("Ubuntu 22 bold"))
titulo.place(x= 240, y=80)

# ----------- Elementos de Entrada de Dados ---------------- 

def adicionar_material():

    global frame_infos_adicionar

    

    frame_infos_adicionar = Frame(frame_entradas, width=450, height=430, bg= co4)
    frame_infos_adicionar.place(x= 20, y=20)

    titulo_operacao = Label(frame_infos_adicionar, text="Criar Material", bg=co4, fg=co3 ,font=("Ubuntu 22 bold"))
    titulo_operacao.place(x=100, y= 20)

    #Nome
    nome_l = Label(frame_infos_adicionar, text="Material:", bg=co4, fg=co3 ,font=("Ubuntu 12 bold"))
    nome_l.place(x=48, y= 80)

    materiais_estoque = Materiais_Combobox()

    nome_e =ttk.Combobox(frame_infos_adicionar, width=30, values=materiais_estoque)
    nome_e.place(x=120, y=84)

    #Quantidade
    quantidade_l = Label(frame_infos_adicionar, text="Quatidade:", bg=co4, fg=co3 ,font=("Ubuntu 12 bold"))
    quantidade_l.place(x=30, y= 130)

    quantidade_e = Entry(frame_infos_adicionar, width=10, font=("Ubuntu 12"))
    quantidade_e.place(x=120, y=130)


    enderecos = Enderecos_Combobox()
    

    #Endereco
    endereco_l = Label(frame_infos_adicionar, text="Endereço:", bg=co4, fg=co3 ,font=("Ubuntu 12 bold"))
    endereco_l.place(x=30, y= 180)

    endereco_e = ttk.Combobox(frame_infos_adicionar, width=30, values= enderecos)
    endereco_e.place(x=120, y=180)

    user_l = Label(frame_infos_adicionar, text="Usuário:", bg=co4, fg=co3 ,font=("Ubuntu 12 bold"))
    user_l.place(x=48, y= 230)

    user_e = Entry(frame_infos_adicionar, width=20, font=("Ubuntu 12"))
    user_e.place(x=120, y=230)

    

    def adicionar_material_banco():
        
        material = nome_e.get()
        quantidade = quantidade_e.get()
        endereco = endereco_e.get()
        user = user_e.get()


        #CRIAR UMA NOVA LISTA PARA ADICIONAR NA MOVIMENTAÇÃO

        # MATERIAL NOVO
        lista = [material, quantidade, endereco]

        

        if material == "":
            messagebox.showerror(title="Erro", message="Preencha o Material de Forma Correta")
        elif quantidade == "":
            messagebox.showerror(title="Erro", message="Preencha a Quantidade de Forma Correta")
        elif endereco == "":
            messagebox.showerror(title="Erro", message="Preencha o Endereço de Forma Correta")
        elif user == "":
            messagebox.showerror(title="Erro", message="Preencha o Usuário de Forma Correta")
        else:

                Inserir_Materiais(lista)
                Mostrar_Tabela()
                messagebox.showinfo(title="Sucesso", message="Material Criado Com Sucesso!")

                nome_e.delete(0, "end")
                quantidade_e.delete(0, "end")
                endereco_e.delete(0, "end")
                user_e.delete(0, "end")            
                    
        

    #Botao Adicionar
    btn_adicionar = Button(frame_infos_adicionar, text="Criar", overrelief="ridge", relief="raised", cursor="hand2", font=("Ubuntu 14 bold"),bg="#0f0", fg="#fff",command= adicionar_material_banco)
    btn_adicionar.place(x=120, y=270)





    if frame_infos_retirar in frame_entradas:
        frame_infos_retirar.destroy()


icone_adicionar = PhotoImage(file="C:/Users/lucas/Desktop/Materiais/images/adicionar-produto.png")
botao_adicionar = Button(frame_topo, image= icone_adicionar, text="Criar Material", compound='left', width=150, overrelief="ridge", relief="raised", cursor="hand2",command=adicionar_material)
botao_adicionar.place(x=240, y= 140)



def adicionar_quantidade():

    frame_quantidade_adicionar = Frame(frame_entradas, width=450, height=430, bg= co4)
    frame_quantidade_adicionar.place(x= 20, y=20)

    # TITULO
    titulo_operacao = Label(frame_quantidade_adicionar, text="Adicionar Material", bg=co4, fg=co3 ,font=("Ubuntu 22 bold"))
    titulo_operacao.place(x=100, y= 20)

    #Nome
    nome_l = Label(frame_quantidade_adicionar, text="Material:", bg=co4, fg=co3 ,font=("Ubuntu 12 bold"))
    nome_l.place(x=48, y= 80)

    materiais_estoque = Materiais_Combobox()

    nome_e =ttk.Combobox(frame_quantidade_adicionar, width=30, values=materiais_estoque)
    nome_e.place(x=120, y=84)

    #Quantidade
    quantidade_l = Label(frame_quantidade_adicionar, text="Quatidade:", bg=co4, fg=co3 ,font=("Ubuntu 12 bold"))
    quantidade_l.place(x=30, y= 130)

    quantidade_e = Entry(frame_quantidade_adicionar, width=10, font=("Ubuntu 12"))
    quantidade_e.place(x=120, y=130)

    enderecos = Enderecos_Combobox()
    

    #Endereco
    endereco_l = Label(frame_quantidade_adicionar, text="Endereço:", bg=co4, fg=co3 ,font=("Ubuntu 12 bold"))
    endereco_l.place(x=30, y= 180)

    endereco_e = ttk.Combobox(frame_quantidade_adicionar, width=30, values= enderecos)
    endereco_e.place(x=120, y=180)


    # User
    user_l = Label(frame_quantidade_adicionar, text="Usuário:", bg=co4, fg=co3 ,font=("Ubuntu 12 bold"))
    user_l.place(x=48, y= 230)

    user_e = Entry(frame_quantidade_adicionar, width=20, font=("Ubuntu 12"))
    user_e.place(x=120, y=230)

    def adicionar_quantidade_banco():

        material = nome_e.get()
        quantidade = quantidade_e.get()
        quantidade_int = int(quantidade)
        endereco = endereco_e.get()
        user = user_e.get()


        if material == "":
            messagebox.showerror(title="Erro", message="Preencha Material de Forma Correta")
        elif quantidade == "":
            messagebox.showerror(title="Erro", message="Preencha a Quantidade de Forma Correta")
        elif user == "":
            messagebox.showerror(title="Erro", message="Preencha o Usuário de Forma Correta")
        else:

            # VERIFICANDO ITEM EXISTENTE
            material_existente = Mostrar_Estoque()

            for item in material_existente:

                material_nome = item[1]
                endereco_alocado = item[3]
                print("Nome do material no banco", material_nome, "Enderço: ", endereco_alocado)
                print("Nome do material na Entry", material, "Endereco da Entry: ",endereco,"\n")

                if (material == material_nome and endereco == endereco_alocado):
                    
                    
                        print(material_nome, "É igual a : ",material)

                        # Pegando o ID
                        item_id = item[0]
                        saldo_atual_banco = item[2]     #Buscando Quantidade no banco
                        saldo_atual_banco_int = int(saldo_atual_banco)

                        saldo_atual = quantidade_int    # Quantidade Entry

                        saldo_entrada = saldo_atual_banco_int + saldo_atual # Quantidade Atualizada

                        dados_entrada = [material, saldo_entrada, item_id]

                        Atualizar(dados_entrada)
                        Mostrar_Tabela()

                        messagebox.showinfo(title="Sucesso", message="Quantidade Acrescida com Sucesso!")

                        nome_e.delete(0, "end")
                        quantidade_e.delete(0, "end")
                        endereco_e.delete(0,"end")
                        user_e.delete(0, "end")
                    
        
           

    btn_adicionar_quantidade = Button(frame_quantidade_adicionar, text="Adicionar", overrelief="ridge", relief="raised", cursor="hand2", font=("Ubuntu 14 bold"),bg="#0f0", fg="#fff", command= adicionar_quantidade_banco)
    btn_adicionar_quantidade.place(x=120, y=270)


icone_adicionar_quantidade = PhotoImage(file="C:/Users/lucas/Desktop/Materiais/images/estoque-rotatividade.png")
botao_adicionar_quantidade = Button(frame_topo, image= icone_adicionar_quantidade, text="Adicionar Material", compound='left', width=150, overrelief="ridge", relief="raised", cursor="hand2",command=adicionar_quantidade)
botao_adicionar_quantidade.place(x=420, y= 140)




def retirar_material():

    

    # Pegando dados de retirada
    material = material_e.get()
    quantidade = quantidade_e.get()
    quantidade_int_entrada = int(quantidade)
    endereco = endereco_e.get()
    user = user_e.get()

    if material == "":
        messagebox.showerror(title="Erro", message="Insira o Material de Forma Correta")
    elif quantidade == "":
        messagebox.showerror(title="Erro", message="Insira a Quantidade de Forma Correta")
    elif user == "":
        messagebox.showerror(title="Erro", message="Insira o Usuário de Forma Correta")
    else:

        lista = [material, quantidade_int_entrada]

        lista_retirada = [material, quantidade_int_entrada, user]

        # Posicionamento material/quantidade
        material_retirada = lista[0]
        quantidade_retirada = lista[1]

        print(quantidade_retirada)
        print(material_retirada,'\n')
        
        # Buscando no banco Todos os materiais
        materiais = Verificar_Quantidade()
        
        

        for item in materiais:

            # NOME DO MATERIAL
            material_nome = item[1]
            endereco_alocado = item[3]

            

            if (material_retirada == material_nome and endereco == endereco_alocado):
                print(item, "Este é o produto!!!")

                # Pegando o id do item
                id = item[0]

                # Pegando quantidade disponivel
                quantidade_material = item[2]
                quantidade_material_int = int(quantidade_material)

                    # QUANTIDADE ENTRY          QUANTIDADE BANCO
                if (quantidade_int_entrada > quantidade_material_int):

                    messagebox.showerror(title="Quantidade Indisponivel", message="Quantidade de retirada maior que disponibilidade no estoque!")

                else:

                    # VALOR SUBTRAIDO
                    saldo = quantidade_material_int - quantidade_int_entrada

                    # DADOS CORRETOS PARA ATUALIZAÇÃO
                    dados_atualizar_estoque = [material, saldo, id]

                    Atualizar(dados_atualizar_estoque)
                    Mostrar_Tabela()

                    messagebox.showinfo(title="Sucesso", message="Material Retirado com sucesso!")

                    material_e.delete(0, "end")
                    quantidade_e.delete(0, "end")
                    endereco_e.delete(0, "end")
                    user_e.delete(0, "end")



def retirar_material_btn():
    global frame_infos_retirar, material_e, quantidade_e, endereco_e, user_e

    

    frame_infos_retirar = Frame(frame_entradas, width=450, height=430, bg= co4)
    frame_infos_retirar.place(x= 20, y=20)

    titulo_operacao = Label(frame_infos_retirar, text="Retirar Material", bg=co4, fg=co3 ,font=("Ubuntu 22 bold"))
    titulo_operacao.place(x=120, y= 20)

    #Material a ser Retirado
    material_l = Label(frame_infos_retirar, text="Material:", bg=co4, fg=co3 ,font=("Ubuntu 12 bold"))
    material_l.place(x=48, y= 80)

    # Buscando Valores no banco
    materiais_estoque = Materiais_Combobox()

    material_e = ttk.Combobox(frame_infos_retirar, width=30, values=materiais_estoque)
    material_e.place(x=120, y=84)

    #Quantidade a ser Retirada
    quantidade_l = Label(frame_infos_retirar, text="Quatidade:", bg=co4, fg=co3 ,font=("Ubuntu 12 bold"))
    quantidade_l.place(x=30, y= 130)

    quantidade_e = Entry(frame_infos_retirar, width=10, font=("Ubuntu 12"))
    quantidade_e.place(x=120, y=130)

    #Enderecos
    enderecos = Enderecos_Combobox()

    endereco_l = Label(frame_infos_retirar, text="Endereço:", bg=co4, fg=co3 ,font=("Ubuntu 12 bold"))
    endereco_l.place(x=30, y= 180)

    endereco_e = ttk.Combobox(frame_infos_retirar, width=20, values= enderecos)
    endereco_e.place(x=120, y=180)

    #Usuário de retirada de material
    user_l = Label(frame_infos_retirar, text="Usuário:", bg=co4, fg=co3 ,font=("Ubuntu 12 bold"))
    user_l.place(x=48, y= 230)

    user_e = Entry(frame_infos_retirar, width=20, font=("Ubuntu 12"))
    user_e.place(x=120, y=230)

    #Botão Retirada de Material
    btn_retirar = Button(frame_infos_retirar, text="Retirar", overrelief="ridge", relief="raised", cursor="hand2", font=("Ubuntu 14 bold"),bg="#0f0", fg="#fff", command= retirar_material)
    btn_retirar.place(x=120, y=270)

    if frame_infos_adicionar in frame_entradas:
        frame_infos_adicionar.destroy()



icone_retirar = PhotoImage(file="C:/Users/lucas/Desktop/Materiais/images/remover.png")
botao_retirar = Button(frame_topo, image= icone_retirar, text="Retirar Material", compound='left', width=150, overrelief="ridge", relief="raised", cursor="hand2", command=retirar_material_btn)
botao_retirar.place(x=600, y= 140)

# titulo_estoque_container = Frame(frame_topo, width=350, height= 60, bg=co1)
# titulo_estoque_container.place(x=780, y= 130)

# titulo_estoque = Label(titulo_estoque_container, text="Estoque", font=("Ivy 22 bold"), bg=co1)
# titulo_estoque.place(x= 120, y= 15)

def movimentacoes():
    
    Movimentacoes_Tela = Toplevel()
    Movimentacoes_Tela.title("Movimentações de Estoque")
    icone = PhotoImage(file="C:/Users/lucas/Desktop/Materiais/images/parcela.png")
    Movimentacoes_Tela.iconphoto(False, icone)
    Movimentacoes_Tela.configure(bg= co1)
    Movimentacoes_Tela.state('zoomed') 
    


    # -------- FRAMES ---------------------

    frame_filtros_expandido = Frame(Movimentacoes_Tela, width=420, height=760, bg=co2)
    frame_filtros_expandido.grid(column=0, row= 0)

    frame_tabela_expandido = Frame(Movimentacoes_Tela, width=920, height=580, bg=co4)
    frame_tabela_expandido.grid(column=1, row= 0)



   
    # ----------- COMPONENTES ------------
    titulo_movimentacoes = Label(frame_filtros_expandido, text="Movimentações", font=("Ivy 22 bold"), bg=co2, fg= co3, )
    titulo_movimentacoes.place(x= 100, y= 15)

    operacao_l = Label(frame_filtros_expandido, text="Operação:", font=("Ivy 14 bold"), bg=co2, fg= co3)
    operacao_l.place(x= 50, y= 80)

    operacoes = ["Entrada","Retirada"]
    operacao_e = ttk.Combobox(frame_filtros_expandido, width=30, values= operacoes)
    operacao_e.place(x=160, y=83)

    material_l_filtro = Label(frame_filtros_expandido, text="Material:", font=("Ivy 14 bold"), bg=co2, fg= co3)
    material_l_filtro.place(x= 52, y= 120)

    materiais = Materiais_Combobox()
    materiais_e_filtro = ttk.Combobox(frame_filtros_expandido, width=30, values= materiais)
    materiais_e_filtro.place(x=160, y=123)

    








    Movimentacoes_Tela.mainloop()



# Botao Movimentacoes 
icone_movimentacoes = PhotoImage(file="C:/Users/lucas/Desktop/Materiais/images/movimentacoes.png")
botao_movimentacoes = Button(frame_topo, image= icone_movimentacoes, text="Movimentações", compound='left', width=150, overrelief="ridge", relief="raised", cursor="hand2", command= movimentacoes)
botao_movimentacoes.place(x=780, y= 140)



def Atualizar_tabela():
    Tabela.destroy()
    Mostrar_Tabela()


# Botao Atualizar Tabela
icone_atualizar = PhotoImage(file="C:/Users/lucas/Desktop/Materiais/images/atualizar.png")

botao_atualizar = Button(frame_topo, image= icone_atualizar, text="Atualizar", compound='left', width=100, overrelief="ridge", relief="raised", cursor="hand2", command= Atualizar_tabela)

botao_atualizar.place(x=1200, y= 140)


#  -------------- Tabela de Vizualização de Itens -------------

Tabela_Estoque_Frame = Frame(Home, width= 830, height= 430, bg= co3)
Tabela_Estoque_Frame.place(x= 500 , y= 220 )


def Mostrar_Tabela():
    global Tabela

    dados = Mostrar_Estoque()

    Tabela_Head = ["Id", "Material", "Quantidade", "Endereço"]

   
    style = ttk.Style() 
    # Configurando Um tema
    style.theme_use("alt")


    # Criando Estilo Tabela
    style.configure("Treeview", 
        background = "silver",
        foreground = "#000",
        rowheight = 25,
        fieldbackground = "silver",
        font = ("Roboto 11")
    )

    style.map("Treeview", 
        background = [('selected', '#606060')]
    )


    Tabela = ttk.Treeview(Tabela_Estoque_Frame, selectmode="browse", columns= Tabela_Head, show="headings", height=16)

    vscb = ttk.Scrollbar(Tabela_Estoque_Frame, orient="vertical", command= Tabela.yview)
    hscb = ttk.Scrollbar(Tabela_Estoque_Frame, orient= "horizontal", command= Tabela.xview)

    Tabela.configure( yscrollcommand= vscb.set, xscrollcommand= hscb.set)
    

    #Posicionando Elementos da tabela
    Tabela.grid(column= 0, row= 0, sticky= "nsew")
    vscb.grid(column= 1, row= 0, sticky= "ns")
    hscb.grid(column=0, row= 1, sticky= "ew")

    
    # Contador
    n = 0
    for coluna in Tabela_Head:
        Tabela.heading(coluna, text= coluna.title(), anchor="center")
        Tabela.column(coluna, width=205, anchor="center")

        n + 1
    
    for item in dados:
        Tabela.insert('', 'end', values= item)
Mostrar_Tabela()


Home.mainloop()

