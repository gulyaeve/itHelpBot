import logging

import requests
import logging
import json

from config import link, headers


def get_id(email):
    try:
        route = f"people?primary_email={email}"
        r = requests.get(f'{link}{route}', headers=headers)
        id4me = r.json()[0]["id"]
        logging.log(msg=f"Found id4me[{id4me}]; email[{email}]", level=logging.INFO)
        return r.json()[0]["id"]
    except Exception as _ex:
        logging.log(msg=f"{_ex}: Unknown email[{email}]", level=logging.INFO)
        return 0

