# import os
from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

# Telegram auth:
telegram_token = env.str("TELEGRAM_API_TOKEN")

# Email auth:
email_server = env.str("EMAIL_SERVER")
email_port = env.int("EMAIL_PORT")
sender_email = env.str("SENDER_EMAIL")
email_login = env.str("EMAIL_LOGIN")
email_password = env.str("EMAIL_PASSWORD")

# 4me Rest API auth:
link = env.str("LINK_4ME")
token = env.str("TOKEN_4ME")
account_id = env.str("ACCOUNT_4ME")
headers = {"Authorization": f"Bearer {token}", "X-4me-Account": account_id}
id_for_request = env.str("ID_FOR_REQUEST")

# Bot admins
bot_admin = env.str("BOT_ADMIN")

# PostgreSQL
DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_HOST = env.str("DB_HOST")
DB_PORT = env.int("DB_PORT")
DB_NAME = env.str("DB_NAME")
