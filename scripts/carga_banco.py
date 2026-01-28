import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from logger_config import get_logger

# Carrega variáveis do .env
load_dotenv()

logger = get_logger()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, os.getenv("DATABASE_DIR"), "operacao.db")
CSV_PATH = os.path.join(BASE_DIR, os.getenv("DATA_TRATADO_DIR"), "dados_tratados.csv")

engine = create_engine(f"sqlite:///{DB_PATH}")


def carregar_banco():
    if not os.path.exists(CSV_PATH):
        logger.error("Arquivo de dados tratados não encontrado. Carga cancelada.")
        return False

    df = pd.read_csv(CSV_PATH)

    if df.empty:
        logger.warning("Arquivo de dados tratados está vazio. Nada para carregar.")
        return False

    df.to_sql("fato_operacao", engine, if_exists="replace", index=False)
    logger.info(f"{len(df)} registros carregados no banco com sucesso.")
    return True


if __name__ == "__main__":
    sucesso = carregar_banco()
    if not sucesso:
        exit(1)
