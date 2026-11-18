# Configuração inicial do banco de dados SQLite para o LabAgenda
import sqlite3

def init_db():
    conn = sqlite3.connect('labagenda.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turma TEXT NOT NULL,
            data TEXT NOT NULL,
            horario TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
