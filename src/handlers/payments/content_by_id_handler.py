from tornado import web, gen
from json import dumps
from tornado.httpclient import AsyncHTTPClient
from tornado.options import options


class ContentbyIdHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        id = self.get_argument("id", None)
        if not id:
            self.set_status(206, dumps({"error": "missing id"}))
            return
        else:
            try:
                url = "{}/content_by_id?id={}".format(
                    options.payments_server_url, id)
                http_client = AsyncHTTPClient()
                response = yield http_client.fetch(url)
                self.write(response.body)
            except Exception as e:
                self.set_status(response.code, str(e))
