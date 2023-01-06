import sqlite3

conn = sqlite3.connect("materiais.db")

with conn:
    cur = conn.cursor()

    query = """
        CREATE TABLE movimentacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            material TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            endereco TEXT NOT NULL,
            data DATE,
            usuario TEXT NOT NULL
        )
    """
    cur.execute(query)

print("Tabela Criada com Sucesso!")