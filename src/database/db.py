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
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        idade INTEGER
    )
    ''')
    conn.commit()
    conn.close()


def inserir_usuario(nome, idade):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', (nome, idade))
    conn.commit()
    conn.close()


def consultar_usuarios():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    rows = cursor.fetchall()
    conn.close()
    return rows
