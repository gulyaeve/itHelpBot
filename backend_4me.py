import requests
from logging import log, INFO

from config import link, headers
from utils import utilities


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
    return utilities.make_dict(r.json(), "id", "name")


def get_service_instance(id_s):
    route = f'service_instances?service={id_s}'
    r = requests.get(f'{link}{route}', headers=headers)
    return utilities.make_dict(r.json(), "id", "name")


def get_subject(id_s):
    route = f'request_templates/enabled?service={id_s}'
    r = requests.get(f'{link}{route}', headers=headers)
    return utilities.make_dict(r.json(), "id", "subject")


def send_request(id4me, subject, comment, id_si):
    post_request = 'requests'
    post_data = f"""{{
        "category": "incident",
        "created_by": "{str(id4me)}",
        "internal_note": "{comment}",
        "requested_by": "{str(id4me)}",
        "subject": "{subject}",
        "service_instance_id": "{str(id_si)}",
        "impact": "low"
        }}"""
    p = requests.post(f'{link}{post_request}',
                      headers=headers,
                      data=str(post_data).encode('Utf-8')
                      )
    return p.json()






