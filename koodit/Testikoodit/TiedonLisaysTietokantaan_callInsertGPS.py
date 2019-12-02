#!/usr/bin/python
from gps import *
import time, inspect, os
import MySQLdb #https://www.tutorialspoint.com/python/python_database_access.htm

db=MySQLdb.connect("stulinux52.ipt.oamk.fi","ubuntu","antenni2","GeoPark")
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

cursor=db.cursor()

print "yhteys saatu"
try:
    
    while True:
        report = gpsd.next() #
        if report['class'] == 'TPV':
            lat = str(getattr(report,'lat',0.0))
            lon = str(getattr(report,'lon',0.0))
            aika = time.strftime("%Y%m%d%H%M%S")
#	    cursor = db.cursor()
	    sql = "INSERT INTO GPS(Aikaleima,Lattitude,Longitude) VALUES(%s,%s,%s)" % (aika,lat,lon)
            cursor.execute(sql)
   	    db.commit()
	    print aika, lat, lon
            break
except:
       db.rollback()

db.close()
