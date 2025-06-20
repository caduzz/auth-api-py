import sqlite3

def create_table():
  conexao = sqlite3.connect('meu_banco.db')
  cursor = conexao.cursor()

  cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE
    )
  ''')

  conexao.commit()
  conexao.close()