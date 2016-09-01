import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
import os
from dbutil import DBUtil


class Application(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class InsertHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('insert.html')

    def post(self):
        name = self.get_argument('name')
        age = int(self.get_argument('age'))
        city = self.get_argument('city')

        db = DBUtil('Info.db', 'information')
        db.insert(name, age, city)
        db.close()
        
        self.redirect('/insert')


class GetHandler(tornado.web.RequestHandler):
    def get(self):
        db = DBUtil('Info.db', 'information')
        data = json.dumps(db.getUsers())
        with open('data.json', 'w+') as outfile:
            json.dump(data, outfile)
        db.close()

        self.render('show.html')


class Jason(tornado.web.RequestHandler):
    def get(self):
        db = DBUtil('Info.db', 'information')
        data = json.dumps(db.getUsers())
        self.write(data)


if __name__ == '__main__':
	app = tornado.web.Application(handlers=[(r'/', Application), (r'/insert', InsertHandler), (r'/show', GetHandler), (r'/jason', Jason)])
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
