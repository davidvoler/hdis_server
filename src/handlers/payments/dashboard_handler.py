from tornado import web, gen
from json import dumps
from tornado.httpclient import AsyncHTTPClient
from tornado.options import options

class DashboardHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        try:
            url = "{}/dashboard".format(
                options.payments_server_url)
            http_client = AsyncHTTPClient()
            response = yield http_client.fetch(url)
            self.write(response.body)
        except Exception as e:
            self.set_status(response.code, str(e))
