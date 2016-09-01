import sqlite3
import json

conn = sqlite3.connect('Info.db')
c = conn.cursor()
c.execute('''CREATE TABLE information (ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, city TEXT);''')
conn.commit()
conn.close()
