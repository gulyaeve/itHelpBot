import smtplib
from logging import log, INFO
from email.mime.text import MIMEText
from config import sender_email, email_password


async def send_email(recipient, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    try:
        server.login(sender_email, email_password)
        msg = MIMEText(message)
        msg["Subject"] = "itHelpBot Authorization"
        server.sendmail(sender_email, recipient, msg.as_string())
        log(msg=f"Success email[{recipient}]: {message}", level=INFO)
    except Exception as _ex:
        log(msg=f"{_ex}: Failed to send email[{recipient}]", level=INFO)
