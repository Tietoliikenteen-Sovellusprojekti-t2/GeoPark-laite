#! /usr/bin/python
from gps import *
import time, inspect, os

#time.sleep(5)
#Kokeilumilelessa 5s tauko

os.chdir(r'/home/pi/DatanKeruu')

f = open(time.strftime("%Y%m%d-%H%M%S")+'_GPSData.txt','w')

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

try:
    
    while True:
        report = gpsd.next() #
        if report['class'] == 'TPV':
            lat = str(getattr(report,'lat',0.0))
            lon = str(getattr(report,'lon',0.0))

            print  lat,"\t",
            print  lon,"\t",
	    print time.strftime("%Y%m%d-%H%M%S"),"\t"

            f.write(lat + '\n')
	    f.write(lon + '\n')
            f.write(time.strftime("%Y%m%d-%H%M%S") + '\r')
            break
except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "Done.\nExiting."
    f.close()
