import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARQUIVO_DADOS = os.path.join(BASE_DIR, "data", "dados.csv")

def carregar_dados():
    """Carrega os dados do arquivo CSV."""
    try:
        df = pd.read_csv(ARQUIVO_DADOS)
        return df
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return None

def buscar_funcionario(nome):
    """Busca funcionários pelo nome."""
    df = carregar_dados()
    if df is not None:
        resultado = df[df['nome'].str.contains(nome, case=False, na=False)]
        return resultado if not resultado.empty else "Nenhum funcionário encontrado."
    return "Erro ao buscar dados."