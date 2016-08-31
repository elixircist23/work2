import sqlite3
import json


class DBUtil():
	def __init__(self):
		self.conn = sqlite3.connect('example.db')
		self.c = self.conn.cursor()		

	def insert(self, name, age):
		self.c.execute('INSERT INTO book (name, age) VALUES (\'%s\', %s);' % (name, age))
	
	def query(self, columnList):
		finalString = ''
		for i in columnList:
			finalString += i + ','
		finalString = finalString[:len(finalString) - 1]
		
		for i in self.c.execute('select %s from book' % finalString):
			print(i)			

	def close(self):
		self.conn.commit()
		self.c.close()

	def jason(self):
		self.close()

		conn = sqlite3.connect('example.db')
		conn.row_factory = sqlite3.Row
		c = conn.cursor()

		c.execute('select * from book')
		recs = c.fetchall()
		rows = [ dict(rec) for rec in recs ]
		rows_json = json.dumps(rows)

		return rows_json


db = DBUtil()
print(db.jason())
db.close()










