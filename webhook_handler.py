from logging import log, INFO

import aiohttp
from aiohttp import web

from config import bot_admin
from loader import bot

routes = web.RouteTableDef()


async def send_json(route, data):
    """
    Send post request to host
    @param route: request link
    @param data: json object to send
    @return: json object from host
    """
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{route}',
                                data=str(data).encode('Utf-8'),
                                ssl=False
                                ) as p:
            return await p.json()


@routes.post('/request')
async def hello(request):
    log(INFO, f"POST request: {request}")
    try:
        data = await request.json()
        if data["event"] == "webhook.verify":
            log(INFO, f"Try to verify")
            callback = data["payload"]["callback"]
            reply = {'message': 'webhook.verify'}
            answer = await send_json(callback, reply)
            log(INFO, f"Answer from verify: {answer}")
        else:
            log(INFO, f"Succses webhook answer:")
            log(INFO, f"{data}")
            await bot.send_message(bot_admin, f"Webhook message: {data['payload']}")
    except:
        log(INFO, f"WRONG POST request: {request}")
        await bot.send_message(1130538822, f"{request}")
    return web.Response(text="{'message':'webhook.verify'}")


app = web.Application()
app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app, port=5000)