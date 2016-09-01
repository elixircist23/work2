import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
from dbutil import DBUtil

class Application(tornado.web.RequestHandler):
	def get(self):
		self.render('insert.html')
		
class InsertHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('testing')
	def post(self):
		name = self.get_argument('name')
		age = int(self.get_argument('age'))
		city = self.get_argument('city')
		
		db = DBUtil('Info.db', 'information')
		db.insert(name, age, city)
		db.close()
		
class GetHandler(tornado.web.RequestHandler):
	def get(self):
		db = DBUtil('Info.db', 'information')
		data = json.dumps(db.getUsers())
		self.write(data)
		db.close()
	
	

if __name__ == '__main__':
	app = tornado.web.Application(handlers =[(r'/', Application), (r'/insert', InsertHandler), (r'/show', GetHandler)])
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(8888)
	tornado.ioloop.IOLoop.instance().start()