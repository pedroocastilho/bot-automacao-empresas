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

## 🔧 Como Instalar e Rodar o Bot

### **1️⃣ Clonar o Repositório**
Se ainda não tem o código, faça o clone do repositório:

```bash
git clone https://github.com/seuusuario/bot-automacao-empresas.git
cd bot-automacao-empresas

2️⃣ Criar o Ambiente Virtual (Opcional, mas Recomendado)
Para evitar conflitos com pacotes do sistema, é recomendado criar um ambiente virtual:
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

3️⃣ Instalar as Dependências
Agora, instale as dependências do projeto:

pip install -r requirements.txt

 4️⃣ Configurar o Arquivo .env
O bot precisa de um e-mail para enviar os relatórios.
Crie um arquivo chamado .env na raiz do projeto e adicione suas credenciais do Gmail:
EMAIL_REMETENTE=seu_email@gmail.com
SENHA=sua_senha_de_aplicativo

📌 IMPORTANTE:
No Gmail, ative a Verificação em Duas Etapas e gere uma Senha de Aplicativo para usar no .env.
NUNCA adicione suas credenciais diretamente no código.

5️⃣ Executar o Bot
Agora, basta rodar o bot no terminal:

python src/main.py

Agora o menu interativo do bot será exibido e você poderá buscar funcionários, gerar relatórios e enviar e-mails automaticamente! 🚀

📧 Configuração do E-mail (Importante!)
Para o envio de e-mails funcionar, siga estes passos:

Acesse sua conta Google e vá para Gerenciar Conta.
Ative a Verificação em Duas Etapas.
Crie uma Senha de Aplicativo e use no .env como SENHA.
Se preferir, ative o "Acesso a apps menos seguros" (não recomendado).

🛠 Melhorias Futuras
🚀 Adicionar uma interface gráfica (GUI)
📊 Criar dashboard com análise de dados
🤖 Implementar chatbot para consultas

📜 Licença
Este projeto é licenciado sob a MIT License.

🚀 Autor
Feito por Pedro Castilho
📧 Contato: pedrocastilho15@hotmail.com.br
🔗 LinkedIn: https://www.linkedin.com/in/pedro-castilho-b03120356/
🔗 GitHub: https://github.com/pepe1528

