from sqlalchemy import create_engine
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "operacao.db")

engine = create_engine(f"sqlite:///{DB_PATH}")

print(f"Banco criado em: {DB_PATH}")
