import matplotlib.pyplot as plt
import seaborn as sns


def configurar_estilo():
    sns.set_theme(style='whitegrid', palette='muted')
    plt.rcParams['figure.figsize'] = (10, 5)


def salvar_figura(fig, nome: str, pasta='reports/figures'):
    fig.tight_layout()
    fig.savefig(f'{pasta}/{nome}', dpi=150)
