import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from consulta import buscar_funcionario
from relatorio import gerar_relatorio
from email_sender import enviar_email

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELATORIO_DIR = os.path.join(BASE_DIR, "reports")

def menu():
    while True:
        print("\n===== Bot de Automação =====")
        print("1. Buscar Funcionário")
        print("2. Gerar Relatório")
        print("3. Enviar Relatório por E-mail")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do funcionário: ")
            resultado = buscar_funcionario(nome)
            if isinstance(resultado, str):
                print("⚠️ Funcionário não encontrado.")
            else:
                print(resultado)

        elif opcao == "2":
            nome = input("Digite o nome do funcionário para gerar o relatório: ")
            gerar_relatorio(nome)

        elif opcao == "3":
            email = input("Digite o e-mail do destinatário: ")
            nome = input("Digite o nome do funcionário: ")
            arquivo = os.path.join(RELATORIO_DIR, f"relatorio_{nome}.pdf")
            if not os.path.exists(arquivo):
                print("⚠️ O relatório não existe. Gere um relatório antes de enviar!")
            else:
                enviar_email(email, arquivo)

        elif opcao == "4":
            print("✅ Saindo...")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()