import smtplib
from email.mime.text import MIMEText
import aiosmtplib
# from email.message import EmailMessage
from logging import log, INFO
from config import sender_email, email_password, email_server, email_port, email_login


async def send_email(recipient, message):
    try:
        # server = aiosmtplib.SMTP(email_server, email_port, timeout=1)
        # smtplib.SMTP(email_server, email_port, timeout=1)
        # await server.starttls()
        # await server.login(email_login, email_password)
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
        # await server.sendmail(sender_email, recipient, msg.as_string())
        log(msg=f"Success email[{recipient}]: {message}", level=INFO)
        # await server.quit()
    except Exception as _ex:
        log(msg=f"{Exception}: {_ex}: Failed to send email[{recipient}]", level=INFO)