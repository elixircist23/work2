import sqlite3
import json


class DBUtil():
    # constructor initializes the database to the given path
    def __init__(self, path, table):
        self.path = path
        self.table = table
        self.conn = sqlite3.connect(path)
        self.c = self.conn.cursor()

    def insert(self, name, age, city):
        self.c.execute('INSERT INTO %s (name, age, city) VALUES (\'%s\', %s, \'%s\');' % (self.table, name, age, city))

    # query method takes in a list, parses it into a valid sql string, then executes
    def query(self, columnList):

        finalString = ''
        for i in columnList:
            finalString += i + ','
        finalString = finalString[:len(finalString) - 1]

        returnList = []
        for i in self.c.execute('select %s from %s' % (finalString, self.table)):
            returnList.append(i)

        return returnList

    # safely close all database connections
    def close(self):
        self.conn.commit()
        self.c.close()

    def delete(self, column, condition):
        self.c.execute('DELETE FROM %s WHERE %s = %s' % s(self.table, column, condition))

    # return a list of all data from the table
    def getUsers(self):
        self.close()

        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()

        c.execute('select * from %s' % self.table)
        recs = c.fetchall()
        rows = [dict(rec) for rec in recs]
        return rows
