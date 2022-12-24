import sqlite3

conn = sqlite3.connect("materiais.db")

with conn:

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE estoque (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            material TEXT NOT NULL,
            quantidade TEXT NOT NULL,
            endereco TEXT NOT NULL
        );
    """)
conn.close()

print("Tabela Criada")