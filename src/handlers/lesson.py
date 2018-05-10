from tornado.gen import coroutine
from handlers.base import BaseHandler
from bson.json_util import dumps
from bson.objectid import ObjectId


class LessonHandler(BaseHandler):
    @coroutine
    def get_all_lessons(self):
      lessons = []
      cursor = yield db['lessons'].find({})
      while (yield cursor.fetch_next):
            doc = cursor.next_object()
            doc['_id'] = str(doc['_id'])
            lessons.append(doc)
      return lessons
    @coroutine
    def get(self):
        id = self.get_argument('id', None)
        if id:
            db = self.get_db()
            lesson = yield db['lessons'].find_one({'_id': ObjectId(id)})
            lesson['id'] = str(lesson['_id'])
            self.write(dumps(lesson))
        else:
            lessons = self.get_all_lessons();
            self.write(dumps(lessons))