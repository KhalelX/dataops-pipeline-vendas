import pandas as pd
import os
from dotenv import load_dotenv
from logger_config import get_logger

# Carrega variáveis do .env
load_dotenv()
logger = get_logger()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTRADA = os.path.join(BASE_DIR, os.getenv("DATA_TRATADO_DIR"), "dados_consolidados.csv")
SAIDA = os.path.join(BASE_DIR, os.getenv("DATA_TRATADO_DIR"), "dados_tratados.csv")


def tratar():
    if not os.path.exists(ENTRADA):
        logger.error("Arquivo consolidado não encontrado. Tratamento cancelado.")
        return False

    df = pd.read_csv(ENTRADA)

    if df.empty:
        logger.warning("Arquivo consolidado está vazio. Nada para tratar.")
        return False

    # Padronizar nomes de colunas
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Remover linhas completamente vazias
    df.dropna(how="all", inplace=True)

    # Padronizar coluna de data, se existir
    if "data" in df.columns:
        df["data"] = pd.to_datetime(df["data"], errors="coerce")

    df.to_csv(SAIDA, index=False)
    logger.info("Tratamento concluído com sucesso.")
    return True


if __name__ == "__main__":
    sucesso = tratar()
    if not sucesso:
        exit(1)
