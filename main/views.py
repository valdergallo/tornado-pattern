import tornado.web
import tornado.httpclient


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("index.html", title="My title", items=items)


class AsyncHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch('http://groovematic.com/', callback=self._on_finish)

    def _on_finish(self, response):
        self.write(str(response.code))
        self.finish()
