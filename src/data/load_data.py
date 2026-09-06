import logging
import pandas as pd
from pathlib import Path
from src.data.gerar_dataset_simulado import gerar_demanda, salvar_dataset

RAW_PATH = Path(__file__).parents[2] / 'data' / 'raw'
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def pipeline_completo() -> pd.DataFrame:
    caminho = RAW_PATH / 'demanda_turnos_simulado.csv'
    if not caminho.exists():
        salvar_dataset(gerar_demanda())
    return pd.read_csv(caminho)
