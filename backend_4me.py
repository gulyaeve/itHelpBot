import requests
import json
from logging import log, INFO

from config import link, headers
from utils import file_system, utilities


def get_id(email):
    try:
        route = f"people?primary_email={email}"
        r = requests.get(f'{link}{route}', headers=headers)
        id4me = r.json()[0]["id"]
        log(msg=f"Found id4me[{id4me}]; email[{email}]", level=INFO)
        return id4me
    except Exception as _ex:
        log(msg=f"{_ex}: Unknown email[{email}]", level=INFO)
        return 0


def get_services():
    route = 'services/enabled'
    r = requests.get(f'{link}{route}', headers=headers)
    # keys = []
    # values = []
    # for item in r.json():
    #     for attribute, value in item.items():
    #         if attribute == "id":
    #             keys.append(value)
    #         if attribute == "name":
    #             values.append(value)
    return utilities.make_dict(r.json(), "id", "name")


def get_service_instance(id_s):
    route = f'service_instances?service={id_s}'
    r = requests.get(f'{link}{route}', headers=headers)
    # values = []
    # for item in r.json():
    #     for attribute, value in item.items():
    #         if attribute == "name":
    #             values.append(value)
    return utilities.make_dict(r.json(), "id", "name")


def get_subject(id_s):
    route = f'request_templates/enabled?service={id_s}'
    r = requests.get(f'{link}{route}', headers=headers)
    return utilities.make_dict(r.json(), "id", "subject")






