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
    CREATE TABLE IF NOT EXISTS endereco (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        estado TEXT NOT NULL,
        cidade TEXT NOT NULL,
        bairro TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


def inserir_moradia(estado, cidade, bairro):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO endereco(estado, cidade, bairro) VALUES (?, ?, ?)', (estado, cidade, bairro))
    conn.commit()
    conn.close()


def consultar_endereco():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM endereco')
    rows = cursor.fetchall()
    conn.close()
    return rows
