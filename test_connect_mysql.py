import MySQLdb

host = "192.168.15.81"
db = MySQLdb.connect(host=host,user='root',passwd='123455',db='moresec')

conn = db.cursor()

conn.execute("select 123");


import pdb;pdb.set_trace()
