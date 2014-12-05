# -*- coding: utf-8 -*-
from MysqlConnection import MysqlConnection
import application


class Connection:
    def __init__(self):
        self.connection = None

        #execute select sentence
        def executeStatement(self, query):
            self.query = query
            try:
                self.connection = MysqlConnection(
                    application.host,
                    application.user,
                    application.password,
                    application.name)
                self.connection.openConnection()
                self.connection.createCursor()
                self.connection.executeStatement(self.query)
                return self.connection.getResults()
            except:
                raise
            finally:
                self.connection.closeConnection()

        #execute insert,drop or update sentence
        def executeUpdate(self, query):
            self.query = query
            try:
                self.connection = MysqlConnection(
                    application.host,
                    application.user,
                    application.password,
                    application.name)
                self.connection.openConnection()
                self.connection.createCursor()
                self.connection.executeStatement(self.query)
                self.connection.executeCommit()
            except:
                self.connection.rollback()
                raise
            finally:
                self.connection.closeConnection()