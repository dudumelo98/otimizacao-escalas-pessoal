"""Gerador simulado de demanda por turno (call center / hospital)."""
import numpy as np
import pandas as pd
from pathlib import Path

RAW_PATH = Path(__file__).parents[2] / 'data' / 'raw'
SEED = 59
DIAS = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
TURNOS = ['Manha', 'Tarde', 'Noite']


def gerar_demanda(seed: int = SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    registros = []
    for dia in DIAS:
        fator_dia = 1.3 if dia in ['Sab', 'Dom'] else 1.0
        for turno in TURNOS:
            fator_turno = {'Manha': 1.2, 'Tarde': 1.0, 'Noite': 0.6}[turno]
            demanda_base = 12 * fator_dia * fator_turno
            demanda = int(rng.poisson(demanda_base))
            registros.append({'dia': dia, 'turno': turno, 'atendimentos_esperados': demanda})
    return pd.DataFrame(registros)


def salvar_dataset(df: pd.DataFrame) -> None:
    RAW_PATH.mkdir(parents=True, exist_ok=True)
    df.to_csv(RAW_PATH / 'demanda_turnos_simulado.csv', index=False)
    print(f'{len(df)} turnos gerados, demanda total: {df["atendimentos_esperados"].sum()}')


if __name__ == '__main__':
    salvar_dataset(gerar_demanda())
