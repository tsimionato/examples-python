import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'examples.db')


def conectar_db():
    conn = sqlite3.connect(DB_PATH)
    return conn


def criar_tabela():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pagamento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dia_pagamento TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


def inserir_pagamento(dia_pagamento):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO pagamento(dia_pagamento) VALUES (?)', (dia_pagamento,))
    conn.commit()
    conn.close()


def consultar_pagamento():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pagamento')
    rows = cursor.fetchall()
    conn.close()
    return rows
