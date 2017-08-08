from aiohttp import web
from typing import Callable


class App(object):
    def __init__(self, host: str= '127.0.0.1', port: str= '8828'):
        self.host = host
        self.port = int(port)
        self.app = None

    def configure(self, url_patterns: (str, str, Callable)):
        app = web.Application()

        for pattern in url_patterns:
            method, url, view = pattern
            app.router.add_route(method, url, view)

        self.app = app

    def run(self):
        web.run_app(self.app, host=self.host, port=self.port)
