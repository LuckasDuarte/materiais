# Pacotes
from tkinter import *
from tkinter import ttk


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

frame_infos_adicionar = Frame(frame_entradas, width=450, height=430, bg= co4)
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

    titulo_operacao = Label(frame_infos_adicionar, text="Adicionar Material", bg=co4, fg=co3 ,font=("Ubuntu 22 bold"))
    titulo_operacao.place(x=100, y= 20)

    #Nome
    nome_l = Label(frame_infos_adicionar, text="Descrição:", bg=co4, fg=co3 ,font=("Ubuntu 12 bold"))
    nome_l.place(x=30, y= 80)

    nome_e = Entry(frame_infos_adicionar, width=30,font=("Ubuntu 12"))
    nome_e.place(x=120, y=84)

    #Quantidade
    quantidade_l = Label(frame_infos_adicionar, text="Quatidade:", bg=co4, fg=co3 ,font=("Ubuntu 12 bold"))
    quantidade_l.place(x=30, y= 130)

    quantidade_e = Entry(frame_infos_adicionar, width=10, font=("Ubuntu 14"))
    quantidade_e.place(x=120, y=130)

    #Endereco
    endereco_l = Label(frame_infos_adicionar, text="Endereço:", bg=co4, fg=co3 ,font=("Ubuntu 12 bold"))
    endereco_l.place(x=30, y= 180)

    endereco_e = Entry(frame_infos_adicionar, width=15, font=("Ubuntu 12"))
    endereco_e.place(x=120, y=180)

    def adicionar_material_banco():
        print("Adicionado")

    #Botao Adicionar
    # logo_adicionar = PhotoImage(file="C:/Users/lucas/Desktop/Materiais/images/adicionar.png")
    btn_adicionar = Button(frame_infos_adicionar, text="Adicionar", overrelief="ridge", relief="raised", cursor="hand2", font=("Ubuntu 14 bold"),bg="#0f0", fg="#fff",command= adicionar_material_banco)
    btn_adicionar.place(x=160, y=240)






    frame_infos_retirar.destroy()


icone_adicionar = PhotoImage(file="C:/Users/lucas/Desktop/Materiais/images/adicionar-produto.png")
botao_adicionar = Button(frame_topo, image= icone_adicionar, text="Adicionar Material", compound='left', width=150, overrelief="ridge", relief="raised", cursor="hand2",command=adicionar_material)
botao_adicionar.place(x=240, y= 140)

def retirar_material():
    global frame_infos_retirar

    

    frame_infos_retirar = Frame(frame_entradas, width=450, height=430, bg= co4)
    frame_infos_retirar.place(x= 20, y=20)

    titulo_operacao = Label(frame_infos_retirar, text="Retirar Material", bg=co4, fg=co3 ,font=("Ubuntu 22 bold"))
    titulo_operacao.place(x=120, y= 20)

    


    frame_infos_adicionar.destroy()



icone_retirar = PhotoImage(file="C:/Users/lucas/Desktop/Materiais/images/remover.png")
botao_retirar = Button(frame_topo, image= icone_retirar, text="Retirar Material", compound='left', width=150, overrelief="ridge", relief="raised", cursor="hand2", command=retirar_material)
botao_retirar.place(x=410, y= 140)

def movimentacoes():
    pass

icone_movimentacoes = PhotoImage(file="C:/Users/lucas/Desktop/Materiais/images/movimentacoes.png")
botao_movimentacoes = Button(frame_topo, image= icone_movimentacoes, text="Movimentações", compound='left', width=150, overrelief="ridge", relief="raised", cursor="hand2")
botao_movimentacoes.place(x=580, y= 140)

Home.mainloop()

# ---------------- CRUD ------------------
