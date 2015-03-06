#!/usr/bin/env python
# coding: utf-8
import tornado.ioloop
from tornado.options import define
from tornado.options import options
from urls import routes
import settings

define("port", default=8000, help="run on the given port", type=int)

application = tornado.web.Application(routes, **settings.CONFIG)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
