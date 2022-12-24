# Pacotes
from tkinter import *


# ------------- Gerar Executável Python: pyinstaller --onefile --noconsole --windowed {Programa} ------#
# -------------- Cores -------------------

co1 = "#ccc"
co2 = "#069"


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

# frame_botoes = Frame(Home, width=1500, height=200, bg= co2)
# frame_botoes.grid(column=0, row=2)

logo = PhotoImage(file="C:/Users/lucas/Desktop/Materiais/images/logo.png", width=200, height=200)    #Logo Santuario
logo_label = Label(frame_topo, image= logo, bg= co1)
logo_label.place(x= 0, y= -20)

titulo = Label(frame_topo, text="Estoque de Materiais", bg=co1, font=("Ubuntu 22 bold"))
titulo.place(x= 240, y=80)

# -------- Adicionar Material, Atualizar Material e Retirar Material ---------

icone_adicionar = PhotoImage(file="C:/Users/lucas/Desktop/Materiais/images/adicionar-produto.png")
botao_adicionar = Button(frame_topo, image= icone_adicionar, text="Adicionar Material", compound='left', width=150, overrelief="ridge", relief="raised", cursor="hand2")
botao_adicionar.place(x=240, y= 140)


icone_retirar = PhotoImage(file="C:/Users/lucas/Desktop/Materiais/images/remover.png")
botao_retirar = Button(frame_topo, image= icone_retirar, text="Retirar Material", compound='left', width=150, overrelief="ridge", relief="raised", cursor="hand2")
botao_retirar.place(x=410, y= 140)


icone_movimentacoes = PhotoImage(file="C:/Users/lucas/Desktop/Materiais/images/movimentacoes.png")
botao_movimentacoes = Button(frame_topo, image= icone_movimentacoes, text="Movimentações", compound='left', width=150, overrelief="ridge", relief="raised", cursor="hand2")
botao_movimentacoes.place(x=580, y= 140)














Home.mainloop()
