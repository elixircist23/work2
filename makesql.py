import sqlite3
import json

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE book (name TEXT, age INTEGER);''')
conn.commit()
conn.close()
