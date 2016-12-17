#!/usr/bin/python3

import pymysql as mariadb
import configparser

config = configparser.ConfigParser()
config.read('connect.cfg')

try:
   conn = mariadb.connect(
     host=config['CONNECTION']['host'],
     user=config['CONNECTION']['user'],
     passwd=config['CONNECTION']['passwd'],
     db=config['CONNECTION']['db'],
     charset=config['CONNECTION']['charset']
   )
   cursor = conn.cursor()
   sql="select version()"
   cursor.execute(sql)
   data = cursor.fetchone()
   print('Database Version is %s' % data)
   cursor.close()
   conn.close()
except Exception as e:
   print('Connection Failed!\nError Code is %s;\nError Content is %s;'%(e.args[0],e.args[1]))


