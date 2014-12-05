# -*- coding: utf-8 -*-
from Connection import *
import logging
import application


class Main:
    def __init__(self):

        print("*** starting program ***")
        logging.basicConfig(filename=application.log, level=logging.ERROR)
        self.connection = None

        try:

            self.connection = Connection()
            results = self.connection.executeStatement("select * from User")

            for row in results:
                print((row[1]))

            self.connection.executeUpdate(
                "insert into User (User_ID) values (1)"
                )

        except Exception as e:
            print(e)
            logging.error(e)

main = Main()
print("*** program ended ***")