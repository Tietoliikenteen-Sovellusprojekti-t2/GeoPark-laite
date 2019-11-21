#!/usr/bin/python

import MySQLdb #https://www.tutorialspoint.com/python/python_database_access.htm

db=MySQLdb.connect("stulinux52.ipt.oamk.fi","ubuntu","antenni2","GeoPark")

cursor = db.cursor()
cursor.execute("SELECT VERSION()") #tahan niita mysql komentoja

data = cursor.fetchone()

print data

db.close()