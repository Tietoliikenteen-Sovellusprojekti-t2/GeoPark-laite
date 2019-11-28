import time, inspect, os
import MySQLdb #https://www.tutorialspoint.com/python/python_database_access.htm'

db=MySQLdb.connect("stulinux52.ipt.oamk.fi","ubuntu","antenni2","GeoPark")

try:
    while True:
        cursor = db.cursor()
        sql = "INSERT INTO Videot(Polku, Nimi) VALUES('aika','lat');"
        print ("Testi Testi")
        cursor.execute(sql)
	db.commit()
	db.close()
