import sys
import asyncio
from aiohttp import web


async def init(loop, address, port):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', home)
    handler = app.make_handler()

    server = await loop.create_server(handler, address, port)
    return server.sockets[0].getsockname()


def main(address='127.0.0.1', port='8888'):
    port = int(port)
    loop = asyncio.get_event_loop()
    host = loop.run_until_complete(init(loop, address, port))
    print(f'Serving on {host}. Hit CTRL-C to stop.')

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    print('Server shutdown.')
    loop.close()


def home(request):
    print('hello server!')
    return web.Response(text='Hello client!')


if __name__ == '__main__':
    main(*sys.argv[1:])
