#!/usr/bin/python3

import mysql.connector
cnx = mysql.connector.connect(user='root',
                              password='admin123',
                              host='127.0.0.1',
                              database='test_database')
cnx.close()
