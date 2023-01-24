import sqlite3



conn = sqlite3.connect("materiais.db")

def Inserir_Materiais(i):
    with conn:
        cur = conn.cursor()
        query = """
            INSERT INTO estoque (material, quantidade, endereco) VALUES (?, ?, ?)
        """
        cur.execute(query, i)
        conn.commit()
        print("Material Criado")

def Mostrar_Estoque():
    with conn:

        cur = conn.cursor()
        lista = []
        query = "SELECT * FROM estoque"

        cur.execute(query)
        dados = cur.fetchall()

        for i in dados:
            lista.append(i)
    return(lista)

def Materiais_Combobox():
    with conn:

        cur = conn.cursor()

        lista = []
        query = "SELECT material FROM estoque"

        cur.execute(query)
        dados = cur.fetchall()

        for i in dados:
            if i not in lista:
                lista.append(i)
        lista.sort()
    return (lista)

def Enderecos_Combobox():
    with conn:

        cur = conn.cursor()

        lista = []
        query = "SELECT endereco FROM estoque"

        cur.execute(query)
        dados = cur.fetchall()

        

        for i in dados:
            if i not in lista:
                lista.append(i)
        lista.sort()

    return(lista)

def Retirar_Material(i):
    with conn:

        cur = conn.cursor()

        lista = []

        query = "UPDATE estoque SET material = ?, quantidade = ?, endereco = ? WHERE id = ? "
        cur.execute(query, i)
        print("Produto Retirado")
    return lista

def Verificar_Quantidade():
    with conn:

        cur = conn.cursor()

        lista = []

        query = "SELECT id, material, quantidade, endereco FROM estoque"
        cur.execute(query)
        dados = cur.fetchall()

        for i in dados:
            lista.append(i)
    return lista

def Atualizar(i):
    with conn:

        cur = conn.cursor()

        query = "UPDATE estoque SET material = ?, quantidade = ? WHERE id =?"
        cur.execute(query, i)
        Materiais_Combobox()
        Enderecos_Combobox()
        print("Atualizado")

# ------------ Funcoes Movimentações --------------#





        