import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

EMAIL_REMETENTE = os.getenv("seu email")
SENHA = os.getenv("sua senha")