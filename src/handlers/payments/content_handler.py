from tornado import web
from json import dumps
from tornado.httpclient import AsyncHTTPClient
from tornado.options import options

class ContentHandler(web.RequestHandler):
    def get(self):
        name       = self.get_argument("name", None)
        media_id   = self.get_argument("media_id", "1")
        media_type = self.get_argument("media_type", "1")
        #creator    = self.get_argument("creator", PUBLIC_KEY)
        #price      = self.get_argument("price", "100")

        if not name:
          self.set_status(206, dumps({"error":"missing name"}))
        else:
          try:
              url = "{}/content?name={}&media_id={}&media_type={}".format(options.payments_server_url,name,media_id,media_type)
              http_client = AsyncHTTPClient()
              response = yield http_client.fetch(url)
              self.write(response)
          except Exception as e:
              self.set_status(response.status_code, str(e))
