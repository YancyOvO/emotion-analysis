import pymysql.cursors

def conn():
     conn= pymysql.connect(
         host='localhost',
         port = 3306,
         user='root',
         db ='com_data',
         charset='utf8', 
     )
     return conn

def cs():
     cursor = conn().cursor()
     return cursor

def close():
     cs().close()
     conn().close()
