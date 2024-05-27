import mysql.connector
import sys

class Db_helper:
    def __init__(self):
        try:
            self.conn=mysql.connector.connect (host='localhost',user='root',password='',database='loging_id_info')
            my_coursore=self.conn.cursor()
        except:
            print('some Error occured ')
            sys.exit(0)


        else:
            print('Data base connected ')



