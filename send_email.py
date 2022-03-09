import smtplib
from logging import log, INFO
from email.mime.text import MIMEText
from config import sender_email, email_password, email_server, email_port, email_login


async def send_email(recipient, message):
    try:
        server = smtplib.SMTP(email_server, email_port, timeout=1)
        server.starttls()
        server.login(email_login, email_password)
        msg = MIMEText(message)
        msg["Subject"] = "itHelpBot Authorization"
        server.sendmail(sender_email, recipient, msg.as_string())
        log(msg=f"Success email[{recipient}]: {message}", level=INFO)
        server.quit()
    except Exception as _ex:
        log(msg=f"{_ex}: Failed to send email[{recipient}]", level=INFO)