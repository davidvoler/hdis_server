from tornado import ioloop, web
import re
from tornado.options import define, options, parse_command_line, parse_config_file
from handlers.lesson import  LessonHandler
from handlers.exercise import  ExerciseHandler
from handlers.payments.add_contributor_handler import  AddContributorHandler
from handlers.payments.content_by_id_handler import  ContentbyIdHandler
from handlers.payments.content_handler import  ContentHandler
from handlers.payments.dashboard_handler import  DashboardHandler
from handlers.payments.purchase_handler import  PurchaseHandler






define("port", default=5555, help="run on port", type=int)
define("mongo_host", default='localhost', help="mongo host", type=str)
define("mongo_port", default=27017, help="mongo port", type=int)
define("mongo_db_name", default='tracker', help="mongo database name", type=str)
define("payments_server_url", default='http://localhost:8888/payments/api', help="payments_server_url", type=str)


def api():
    return web.Application([
        (r"/server/api/lesson", LessonHandler),
        (r"/server/api/exercise", ExerciseHandler),
        (r"/server/api/content_by_id", ContentbyIdHandler),
        (r"/server/api/content", ContentHandler),
        (r"/server/api/purchase", PurchaseHandler),
        (r"/server/api/dashboard", DashboardHandler),
    ])

if __name__ == "__main__":
    app = api()
    app.listen(options.port)
    print ("Server running on port {}".format(options.port))
    ioloop.IOLoop.current().start()
