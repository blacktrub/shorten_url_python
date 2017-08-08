from aiohttp import web

from .utils import logging_view


@logging_view
async def home(request: web.Request) -> web.Response:
    return web.Response(text='Hello client!')
