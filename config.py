import os

# Telegram auth:
telegram_token = os.environ.get("TELEGRAM_API_TOKEN")

# Email auth:
email_server = os.environ.get("EMAIL_SERVER")
email_port = int(os.environ.get("EMAIL_PORT"))
sender_email = os.environ.get("SENDER_EMAIL")
email_login = os.environ.get("EMAIL_LOGIN")
email_password = os.environ.get("EMAIL_PASSWORD")

# 4me Rest API auth:
link = os.environ.get("LINK_4ME")
token = os.environ.get("TOKEN_4ME")
account_id = os.environ.get("ACCOUNT_4ME")
headers = {"Authorization": f"Bearer {token}", "X-4me-Account": account_id}
id_for_request = os.environ.get("ID_FOR_REQUEST")

# Bot admins
bot_admin = os.environ.get("BOT_ADMIN")
