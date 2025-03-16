# 📌 Bot de Automação para Empresas 🚀

Este é um **bot de automação** que realiza **consultas, geração de relatórios e envio de e-mails** para empresas e prefeituras.

## 📋 Funcionalidades
✅ Busca de funcionários cadastrados em um banco de dados CSV  
✅ Geração automática de relatórios em PDF  
✅ Envio de relatórios por e-mail  
✅ Interface CLI interativa  

---

## ⚙️ Tecnologias Utilizadas
- **Python 3.13.2**
- **pandas** (Manipulação de dados)
- **fpdf** (Geração de PDFs)
- **smtplib** (Envio de e-mails)
- **dotenv** (Carregar credenciais de ambiente)

---

## 🏗 Estrutura do Projeto

bot-automacao-empresas/ │── data/ # Base de dados CSV
│── reports/ # Relatórios gerados
│── src/ # Código-fonte
│ ├── consulta.py # Busca funcionários
│ ├── relatorio.py # Gera PDFs com os dados
│ ├── email_sender.py # Envia e-mails com os PDFs anexados
│ ├── main.py # Menu interativo do bot
│ ├── config.py # Configuração do bot
│ ├── init.py # Indica que 'src' é um pacote Python
│── .env # (NÃO SUBIR NO GITHUB!) Credenciais do e-mail
│── .gitignore # Ignorar arquivos sensíveis no GitHub
│── README.md # Documentação do projeto
│── requirements.txt # Lista de dependências