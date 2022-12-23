# Pacotes
from tkinter import *

# -------------- Cores -------------------

co1 = "#ccc"
co2 = "#069"


# -------------- Atributos Janela --------------
Home = Tk()
Home.title("Estoque Materiais")
icone = PhotoImage(file="images/parcela.png")
Home.iconphoto(False, icone)
Home.configure(bg= co1)
Home.state('zoomed')    # Preenche toda a tela

frame_topo = Frame(Home, width=1500, height=200,bg= co2)
frame_topo.grid(column=0, row=1)

logo = PhotoImage(file="images/logo.png", width=200, height=200)
logo_label = Label(frame_topo, image= logo, bg= co1)
logo_label.place(x= 0, y=0)










Home.mainloop()
