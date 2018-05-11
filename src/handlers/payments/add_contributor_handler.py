from tornado import web, gen
from json import dumps
from tornado.httpclient import AsyncHTTPClient
from tornado.options import options


class AddContributorHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        media_id    = self.get_argument("media_id")
        #contributor = self.get_argument("contributor", PUBLIC_KEY)
        if not media_id:
            self.set_status(206, dumps({"error": "missing media_id"}))
        else:
            try:
                url = "{}/purchase?media_id={}".format(
                    options.payments_server_url, media_id)
                http_client = AsyncHTTPClient()
                response = yield http_client.fetch(url)
                self.write(response.body)
            except Exception as e:
                self.set_status(500, str(e))
                self.write(dumps({'error':str(e)}))
