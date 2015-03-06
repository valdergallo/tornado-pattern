#!/usr/bin/env python
# coding: utf-8
import tornado.ioloop
from tornado.options import define
from tornado.options import options
from urls import routes
import settings

define("port", default=8888, help="run on the given port", type=int)

def main():
    application = tornado.web.Application(routes, **settings.CONFIG)
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

