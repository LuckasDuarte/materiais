# Pacotes
from tkinter import *

# -------------- Cores -------------------

cinza = "#ccc"


# -------------- Atributos Janela --------------
Home = Tk()
Home.title("Estoque Materiais")
icone = PhotoImage(file="images/parcela.png")
Home.iconphoto(False, icone)
Home.configure(bg= cinza)
Home.state('zoomed')    # Preenche toda a tela













Home.mainloop()
