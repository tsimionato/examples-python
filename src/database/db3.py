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
    CREATE TABLE IF NOT EXISTS Ficha (
        Formação TEXT NOT NULL,
        Trabalho TEXT NOT NULL      
    )
    ''')
    conn.commit()
    conn.close()


def inserir_ficha(formacao, trabalho):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Ficha(formacao, trabalho) VALUES (?, ?)', (formacao, trabalho))
    conn.commit()
    conn.close()


def consultar_ficha():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Ficha')
    rows = cursor.fetchall()
    conn.close()
    return rows
