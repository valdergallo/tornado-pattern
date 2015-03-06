# coding: utf-8
from main.views import MainHandler
from main.views import AsyncHandler
import tornado.web
import settings

routes = [
    (r"/", MainHandler),
    (r"/async/", AsyncHandler),
    # static files
    (r'/static/(.*)', tornado.web.StaticFileHandler,
        {'path': settings.CONFIG.get('static_path')}),
]
