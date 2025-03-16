import smtplib
import os
from email.message import EmailMessage
from src.config import EMAIL_REMETENTE, SENHA

def enviar_email(destinatario, arquivo):
    """Envia um e-mail com o relatório anexado."""
    msg = EmailMessage()
    msg["Subject"] = "Relatório Gerado"
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = destinatario
    msg.set_content("Segue em anexo o relatório solicitado.")

    with open(arquivo, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=os.path.basename(arquivo))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_REMETENTE, SENHA)
            server.send_message(msg)
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")