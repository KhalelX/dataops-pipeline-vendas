import subprocess
import sys
import os
from logger_config import get_logger

logger = get_logger()
PYTHON_EXEC = sys.executable

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def run_script(script_name):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    logger.info(f"Iniciando {script_name}")

    result = subprocess.run([PYTHON_EXEC, script_path], capture_output=True, text=True)

    if result.returncode == 0:
        logger.info(f"{script_name} executado com sucesso.")
        return True
    else:
        logger.error(f"Erro ao executar {script_name}")
        logger.error(result.stderr)
        return False


if __name__ == "__main__":
    logger.info("==== INÍCIO DA PIPELINE ====")

    if not run_script("ingestao.py"):
        logger.error("Pipeline encerrada: falha na ingestão.")
    elif not run_script("tratamento.py"):
        logger.error("Pipeline encerrada: falha no tratamento.")
    elif not run_script("carga_banco.py"):
        logger.error("Pipeline encerrada: falha na carga do banco.")

    logger.info("==== FIM DA PIPELINE ====")
