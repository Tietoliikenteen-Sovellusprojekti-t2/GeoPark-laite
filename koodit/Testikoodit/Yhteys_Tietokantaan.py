#!/usr/bin/python

import MySQLdb

db=MySQLdb.connect("stulinux52.ipt.oamk.fi","ubuntu","antenni2","GeoPark")

cursor = db.cursor()
cursor.execute("DESC GPS;") #tahan niita mysql komentoja

data = cursor.fetchall()

print data

db.close()
