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
        print("Informações Inseridas")