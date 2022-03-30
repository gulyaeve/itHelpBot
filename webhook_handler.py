from aiohttp import web

routes = web.RouteTableDef()


@routes.post('/requests')
async def hello(request):
    data = await request.json()
    print(dict(data))
    return web.Response(text="Hello, world")


app = web.Application()
app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app, port=5000)
