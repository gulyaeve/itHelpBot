from email.mime.text import MIMEText
import aiosmtplib
from logging import log, INFO
from config import sender_email, email_password, email_server, email_port, email_login


async def send_email(recipient, message):
    try:
        msg = MIMEText(message)
        msg["Subject"] = "itHelpBot Authorization"
        await aiosmtplib.send(message=msg,
                              sender=sender_email,
                              recipients=recipient,
                              hostname=email_server,
                              port=email_port,
                              username=email_login,
                              password=email_password,
                              timeout=1,
                              start_tls=True)
        log(msg=f"Success email[{recipient}]: {message}", level=INFO)
    except Exception as _ex:
        log(msg=f"{Exception}: {_ex}: Failed to send email[{recipient}]", level=INFO)