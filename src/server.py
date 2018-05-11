from tornado import ioloop, web
import re
from tornado.options import define, options, parse_command_line, parse_config_file
from handlers.lesson import  LessonHandler
from handlers.exercise import  ExerciseHandler


define("port", default=6666, help="run on port", type=int)
define("mongo_host", default='localhost', help="mongo host", type=str)
define("mongo_port", default=27017, help="mongo port", type=int)
define("mongo_db_name", default='tracker', help="mongo database name", type=str)
define("payments_server_url", default='http://localhost:8888', help="payments_server_url", type=str)



def api():
    return web.Application([
        (r"/api/server/lesson", LessonHandler),
        (r"/api/server/exercise", ExerciseHandler),
    ])

if __name__ == "__main__":
    app = api()
    app.listen(options.port)
    print ("Server running on port {}".format(options.port))
    ioloop.IOLoop.current().start()
