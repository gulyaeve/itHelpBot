import os

# Telegram auth:
telegram_token = os.environ.get("TELEGRAM_API_TOKEN")

# Gmail auth:
sender_email = os.environ.get("SENDER_EMAIL")
email_password = os.environ.get("EMAIL_PASSWORD")

# 4me Rest API auth:
link = os.environ.get("LINK_4ME")
token = os.environ.get("TOKEN_4ME")
account_id = os.environ.get("ACCOUNT_4ME")
headers = {"Authorization": f"Bearer {token}", "X-4me-Account": account_id}