#!/usr/bin/python

import MySQLdb

db=MySQLdb.connect("stulinux52.ipt.oamk.fi","ubuntu","antenni2","GeoPark")

cursor = db.cursor()
#<<<<<<< HEAD
testi1 = str("lol")
testi2 = 'aaa'
testi3 = "sss"
sql = "insert into Videot(Polku, Nimi, Aikaleima) values('lala', 10, 10)"
cursor.execute(sql)
db.commit()
cursor.execute("SELECT VERSION()") #tahan niita mysql komentoja
#>>>>>>> 8481c564b79da8165a55e197e27123bd74acc051

data = cursor.fetchall()

print data

db.close()
