import aiohttp
from logging import log, INFO

from config import link, headers, id_for_request
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
        log(msg=f"{Exception}: {_ex}: Unknown email[{email}]", level=INFO)
        return 0


async def get_services():
    answer = await get_json('services/enabled?provider=694')
    return await utilities.make_dict(answer, "id", "name")


async def get_service_instance(id_s):
    answer = await get_json(f'service_instances?service={id_s}')
    return await utilities.make_dict(answer, "id", "name")


async def get_subject(id_s):
    answer = await get_json(f'request_templates/enabled?service={id_s}')
    return await utilities.make_dict(answer, "id", "subject")


async def send_request(id4me, subject, comment, id_si):
    post_request = 'requests'
    comment = comment.replace('\n', ' ').replace('"', "'")
    post_data = f"""{{
                "requested_by": "{str(id_for_request)}",
                "requested_for": "{str(id4me)}",
                "subject": "{subject}",
                "service_instance_id": "{str(id_si)}",
                "internal_note": "{comment} (Отправлено из чат-бота https://t.me/itHelpDigitalCenter_bot)",
                "category": "incident",
                "impact": "low"
                }}"""
    return await send_json(post_request, post_data)


async def check_admin(id4me):
    answer = await get_json(f'people/{id4me}/teams')
    return answer


async def get_requests_for_team(team):
    answer = await get_json(f'requests/open?team={team}')
    return answer


async def get_requests_for_member(id4me):
    answer = await get_json(f'requests/open?member={id4me}')
    return answer


async def get_request(request_id):
    answer = await get_json(f'requests/{request_id}')
    return answer


async def get_notes_for_request(request_id):
    answer = await get_json(f'requests/{request_id}/notes')
    return answer


async def post_note_to_request(request_id, text):
    post_request = f"requests/{request_id}/notes"
    text = text.replace('\n', ' ').replace('"', "'")
    post_data = f"""{{
                "text": "{text}"
                }}"""
    return await send_json(post_request, post_data)



