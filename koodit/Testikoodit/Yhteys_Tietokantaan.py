#!/usr/bin/python

import MySQLdb

db=MySQLdb.connect("stulinux52.ipt.oamk.fi","ubuntu","antenni2","GeoPark")

cursor = db.cursor()
<<<<<<< HEAD
cursor.execute("DESC GPS;") #tahan niita mysql komentoja
=======
cursor.execute("SELECT VERSION()") #tahan niita mysql komentoja
>>>>>>> 8481c564b79da8165a55e197e27123bd74acc051

data = cursor.fetchall()

print data

db.close()
