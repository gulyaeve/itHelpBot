import requests
import json
from logging import log, INFO

from config import link, headers


def get_id(email):
    try:
        route = f"people?primary_email={email}"
        r = requests.get(f'{link}{route}', headers=headers)
        id4me = r.json()[0]["id"]
        log(msg=f"Found id4me[{id4me}]; email[{email}]", level=INFO)
        return r.json()[0]["id"]
    except Exception as _ex:
        log(msg=f"{_ex}: Unknown email[{email}]", level=INFO)
        return 0

