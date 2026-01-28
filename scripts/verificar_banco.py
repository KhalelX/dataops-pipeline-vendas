import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "operacao.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tabelas:", cursor.fetchall())

cursor.execute("SELECT COUNT(*) FROM fato_operacao;")
print("Linhas:", cursor.fetchone()[0])

conn.close()
