import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1]))
import pandas as pd
from src.models.escala import otimizar_escala, CAPACIDADE_POR_FUNCIONARIO


def test_escala_cobre_demanda():
    df = pd.DataFrame({'dia': ['Seg'], 'turno': ['Manha'], 'atendimentos_esperados': [10]})
    resultado = otimizar_escala(df, n_funcionarios_pool=20)
    alocado = resultado['escala'].iloc[0]['funcionarios_alocados']
    assert alocado * CAPACIDADE_POR_FUNCIONARIO >= 10
