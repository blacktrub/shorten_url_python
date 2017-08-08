import sys
from server.app import App

from server.urls import patterns


if __name__ == '__main__':
    app = App(*sys.argv[1:])

    app.configure(patterns)
    app.run()
