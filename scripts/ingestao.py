import pandas as pd
import os
from dotenv import load_dotenv
from logger_config import get_logger

# Carrega variáveis do .env
load_dotenv()

logger = get_logger()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMINHO_BRUTO = os.path.join(BASE_DIR, os.getenv("DATA_BRUTO_DIR"))
SAIDA = os.path.join(BASE_DIR, os.getenv("DATA_TRATADO_DIR"), "dados_consolidados.csv")


def carregar_dados():
    arquivos = [f for f in os.listdir(CAMINHO_BRUTO) if f.endswith(".xlsx") or f.endswith(".csv")]

    if not arquivos:
        logger.warning("Nenhum arquivo encontrado em data_bruto. Ingestão cancelada.")
        return False

    dfs = []

    for arquivo in arquivos:
        caminho = os.path.join(CAMINHO_BRUTO, arquivo)
        logger.info(f"Lendo {arquivo}")

        if arquivo.endswith(".xlsx"):
            df = pd.read_excel(caminho)
        else:
            df = pd.read_csv(caminho)

        dfs.append(df)

    df_final = pd.concat(dfs, ignore_index=True)
    df_final.to_csv(SAIDA, index=False)
    logger.info("Ingestão concluída com sucesso.")
    return True


if __name__ == "__main__":
    sucesso = carregar_dados()
    if not sucesso:
        exit(1)  # avisa a pipeline que a ingestão falhou
