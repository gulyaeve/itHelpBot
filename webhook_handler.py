from logging import log, INFO

import aiohttp
from aiohttp import web

routes = web.RouteTableDef()


async def get_json(route):
    """
    Send get request to host
    @param route: request link
    @return: json object answer from host
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{route}', ssl=False) as resp:
            return await resp.json()


@routes.post('/request')
async def hello(request):
    log(INFO, f"POST request: {request}")
    print(f"POST request: {request}")
    try:
        log(INFO, f"Try to verify")
        print(f"Try to verify")
        data = await request.json()
        callback = data["payload"]["callback"]
        answer = await get_json(callback)
        log(INFO, f"Answer to verify: {answer}")
        print(f"Answer to verify: {answer}")
    except:
        log(INFO, f"WRONG POST request: {request}")
        print(f"WRONG POST request: {request}")
    return web.Response(text="{'message':'webhook.verify'}")


app = web.Application()
app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app, port=5000)