import requests
import json

from config import link, headers


def get_id(email):
    try:
        route = f"people?primary_email={email}"
        r = requests.get(f'{link}{route}', headers=headers)
        return r.json()[0]["id"]
    except Exception as _ex:
        return f"{_ex}\nCheck email!"

