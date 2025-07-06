import sqlite3

class User:
  def __init__(self):
    self.conn = sqlite3.connect('src/database/meu_banco.db', check_same_thread=False)
    self.cursor = self.conn.cursor()

  def get_by_id(self, user_id: int):
    user = self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    return user

  def get_all(self):
    return self.cursor.execute("SELECT * FROM users").fetchall()

  def create(self, name: str, email: str):
    self.cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    self.conn.commit()
    return {"name": name, "email": email}

  def get_user_by_email(self, email: str):
    user = self.cursor.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    return user