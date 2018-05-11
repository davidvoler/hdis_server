from tornado import web, gen
from json import dumps
from tornado.httpclient import AsyncHTTPClient
from tornado.options import options


class PurchaseHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        content_id = self.get_argument('content_id')
        #student_public_key  = self.get_argument('public_key', PUBLIC_KEY)
        #student_private_key = self.get_argument('private_key', PRIVATE_KEY)
        if not content_id:
            self.set_status(206, dumps({"error": "missing name"}))
        else:
            try:
                url = "{}/purchase?content_id={}".format(
                    options.payments_server_url, content_id)
                http_client = AsyncHTTPClient()
                response = yield http_client.fetch(url)
                self.write(response.body)
            except Exception as e:
                self.set_status(response.code, str(e))
