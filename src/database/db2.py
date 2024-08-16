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
    CREATE TABLE IF NOT EXISTS genero (
        id INTEGER PRIMARY KEY,
        descricao TEXT NOT NULL      
    )
    ''')
    conn.commit()
    conn.close()


def inserir_genero(id, descricao):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO genero (id, descricao) VALUES (?, ?)', (id, descricao))
    conn.commit()
    conn.close()


def consultar_genero():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM genero')
    rows = cursor.fetchall()
    conn.close()
    return rows
