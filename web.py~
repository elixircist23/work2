import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from dbutil import DBUtil

class Application(tornado.web.RequestHandler):
	def get(self):
		db = DBUtil()
		data = db.jason()
		db.close()
		self.write(data)	
	
	

if __name__ == '__main__':
	app = tornado.web.Application(handlers =[(r'/', Application)])
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
