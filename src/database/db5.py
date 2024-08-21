import sqlite3
import os
from datetime import datetime

# Define o caminho do banco de dados
DB_PATH = os.path.join(os.path.dirname(__file__), 'examples.db')


def conectar_db():
    """Conecta ao banco de dados SQLite e retorna a conexão."""
    conn = sqlite3.connect(DB_PATH)
    return conn


def criar_tabela():
    """Cria a tabela 'pagamento' no banco de dados, se não existir."""
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pagamento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_pagamento DATETIME NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


def inserir_pagamento(data_pagamento):
    """Insere um novo registro de pagamento com a data fornecida."""
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO pagamento (data_pagamento) VALUES (?)', (data_pagamento,))
    conn.commit()
    conn.close()


def consultar_pagamento():
    """Consulta todos os registros de pagamentos e retorna os resultados."""
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pagamento')
    rows = cursor.fetchall()
    conn.close()
    return rows
