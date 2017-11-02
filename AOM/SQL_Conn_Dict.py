import pymysql.cursors

def conn():
     conn= pymysql.connect(
         host='localhost',
         port = 3306,
         user='root',
         db ='com_data',
         charset='utf8', 
     )
     cursor = conn.cursor()
     return cursor
#cursor.execute("select * from comment")
#while(True):
#     row_1 = cursor.fetchone()
#     if row_1 == None:
#         break
#     print(row_1)
