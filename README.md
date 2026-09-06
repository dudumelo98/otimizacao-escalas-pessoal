# Otimização de Escalas e Alocação de Pessoal com IA

Escala de turnos otimizada via programação inteira (PuLP), cobrindo demanda simulada e respeitando o limite de 44h semanais da CLT.

## Resultados

- Status do solver: ótimo.
- 59 funcionários-turno na semana, cobrindo demanda de 256 atendimentos esperados com um pool de 25 funcionários.

## Como rodar

```bash
pip install -r requirements.txt
python -m src.data.gerar_dataset_simulado
jupyter notebook notebooks/
pytest tests/
```

Detalhes completos em [reports/relatorio_final.md](reports/relatorio_final.md).
