# -*- coding: utf-8 -*-
import MySQLdb


class MysqlConnection:

    def __init__(self, hostname, user, password, database):
        self.hostname = hostname
        self.user = user
        self.password = password
        self.database = database
        self.db = None
        self.cursor = None
        self.query = None

    def openConnection(self):
        try:
            if (
                self.hostname == None or len(self.hostname) < 1) or (self.user == None or len(self.user) < 1) or (self.password == None or len(self.password) < 1) or (self.database == None or len(self.database) < 1):
                raise Exception("illegal arguments")
            self.db = MySQLdb.connect(
                self.hostname,
                self.user,
                self.password,
                self.database)
        except:
            raise

    def createCursor(self):
        try:
            self.cursor = self.db.cursor()
        except:
            raise

    def executeStatement(self, query):
        self.query = query
        try:
            if self.query is None or len(self.query) < 1:
                raise Exception("error", "query is null or empty")
            self.cursor.execute(self.query)
        except:
            raise

    def executeCommit(self):
        try:
            self.db.commit()
        except:
            raise

    def rollback(self):
        try:
            self.db.rollback()
        except:
            raise

    def getResults(self):
        return self.cursor.fetchall()

    def closeConnection(self):
        try:
            if(self.db is not None):
                self.db.close()
        except:
            raise