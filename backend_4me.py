import aiohttp
from logging import log, INFO

from config import link, headers
from utils import utilities


async def get_json(route):
    """
    Send get request to host
    @param route: request link
    @return: json object answer from host
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{link}{route}', headers=headers, ssl=False) as resp:
            return await resp.json()


async def send_json(route, data):
    """
    Send post request to host
    @param route: request link
    @param data: json object to send
    @return: json object from host
    """
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{link}{route}',
                                headers=headers,
                                data=str(data).encode('Utf-8'),
                                ssl=False
                                ) as p:
            return await p.json()


async def get_id(email):
    try:
        answer = await get_json(f"people?primary_email={email}")
        id4me = answer[0]["id"]
        log(msg=f"Found id4me[{id4me}]; email[{email}]", level=INFO)
        return id4me
    except Exception as _ex:
        log(msg=f"{_ex}: Unknown email[{email}]", level=INFO)
        return 0


async def get_services():
    answer = await get_json('services/enabled')
    return await utilities.make_dict(answer, "id", "name")


async def get_service_instance(id_s):
    answer = await get_json(f'service_instances?service={id_s}')
    return await utilities.make_dict(answer, "id", "name")


async def get_subject(id_s):
    answer = await get_json(f'request_templates/enabled?service={id_s}')
    return await utilities.make_dict(answer, "id", "subject")


async def send_request(id4me, subject, comment, id_si):
    post_request = 'requests'
    post_data = f"""{{
                "created_by": "{str(id4me)}",
                "requested_by": "{str(id4me)}",
                "requested_for": "{str(id4me)}",
                "subject": "{subject}",
                "service_instance_id": "{str(id_si)}",
                "internal_note": "{comment}",
                "category": "incident",
                "impact": "low"
                }}"""
    return await send_json(post_request, post_data)
