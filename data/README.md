# Dados

Demanda simulada por turno (7 dias, 3 turnos), gerada com `numpy`.

## Por que simulado

ILOSTAT e PNAD Contínua trazem estatísticas agregadas de mercado de trabalho, não demanda por turno de uma operação específica. Gerei uma base sintética (`src/data/gerar_dataset_simulado.py`).

## Geração

```bash
python -m src.data.gerar_dataset_simulado
```
