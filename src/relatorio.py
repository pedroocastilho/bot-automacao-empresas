import os
from fpdf import FPDF
import pandas as pd
from src.consulta import buscar_funcionario

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELATORIO_DIR = os.path.join(BASE_DIR, "reports")

def gerar_relatorio(nome):
    """Gera um relatório em PDF para o funcionário pesquisado."""
    resultado = buscar_funcionario(nome)

    if isinstance(resultado, str):
        print(resultado)
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "Relatório de Funcionário", ln=True, align='C')

    pdf.set_font("Arial", size=12)
    for _, row in resultado.iterrows():
        pdf.cell(0, 10, f"Nome: {row['nome']}", ln=True)
        pdf.cell(0, 10, f"Departamento: {row['departamento']}", ln=True)
        pdf.cell(0, 10, f"Salário: R$ {row['salario']}", ln=True)
        pdf.cell(0, 10, "-"*40, ln=True)

    relatorio_nome = os.path.join(RELATORIO_DIR, f"relatorio_{nome}.pdf")
    pdf.output(relatorio_nome)
    print(f"Relatório salvo em {relatorio_nome}")