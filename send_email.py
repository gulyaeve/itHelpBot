import smtplib
from email.mime.text import MIMEText
from config import sender_email, email_password


def send_email(recipient, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    try:
        server.login(sender_email, email_password)
        msg = MIMEText(message)
        msg["Subject"] = "itHelpBot Authorization"
        server.sendmail(sender_email, recipient, msg.as_string())
        print("The message was sent successfully!")
    except Exception as _ex:
        print(f"{_ex}\nCheck your login or password please!")