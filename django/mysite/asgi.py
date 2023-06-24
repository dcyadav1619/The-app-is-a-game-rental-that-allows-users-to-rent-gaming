from some_asgi_library import AmazingMiddleware

application = AmazingMiddleware(application)

async def application(scope, receive, send):
    event = await receive()
    ...
    await send({"type": "websocket.send", ...})