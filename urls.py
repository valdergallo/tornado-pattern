# coding: utf-8
from main.views import MainHandler
import tornado.web
import settings

routes = [
    (r"/", MainHandler),
    # static files
    (r'/static/(.*)', tornado.web.StaticFileHandler,
        {'path': settings.CONFIG.get('static_path')}),
]
