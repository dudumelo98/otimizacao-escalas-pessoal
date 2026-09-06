"""
Otimizacao de escala via programacao inteira (PuLP).

Decide quantos funcionarios alocar em cada turno pra cobrir a demanda
esperada, minimizando o total de funcionarios-turno, respeitando o limite
de horas semanais da CLT (44h) aplicado ao total da equipe disponivel.
"""
import pulp
import pandas as pd

CAPACIDADE_POR_FUNCIONARIO = 5  # atendimentos que 1 funcionario cobre por turno
HORAS_POR_TURNO = 8
LIMITE_HORAS_SEMANAIS_CLT = 44


def otimizar_escala(df_demanda: pd.DataFrame, n_funcionarios_pool: int) -> dict:
    problema = pulp.LpProblem('escala_pessoal', pulp.LpMinimize)

    variaveis = {
        (row['dia'], row['turno']): pulp.LpVariable(f"x_{row['dia']}_{row['turno']}", lowBound=0, cat='Integer')
        for _, row in df_demanda.iterrows()
    }

    problema += pulp.lpSum(variaveis.values())

    for _, row in df_demanda.iterrows():
        var = variaveis[(row['dia'], row['turno'])]
        problema += var * CAPACIDADE_POR_FUNCIONARIO >= row['atendimentos_esperados']

    # Limite de horas: total de horas alocadas na semana nao pode passar do
    # que a equipe disponivel comporta dentro do teto legal da CLT.
    problema += pulp.lpSum(variaveis.values()) * HORAS_POR_TURNO <= n_funcionarios_pool * LIMITE_HORAS_SEMANAIS_CLT

    status = problema.solve(pulp.PULP_CBC_CMD(msg=False))

    resultado = df_demanda.copy()
    resultado['funcionarios_alocados'] = [int(variaveis[(r['dia'], r['turno'])].value()) for _, r in df_demanda.iterrows()]

    return {
        'status': pulp.LpStatus[status],
        'total_funcionarios_turno': int(pulp.value(problema.objective)),
        'escala': resultado,
    }
