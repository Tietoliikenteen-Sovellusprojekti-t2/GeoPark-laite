#! /usr/bin/python
from gps import *
import time, inspect, os
time.sleep(5)

os.chdir(r'/home/pi/DatanKeruu')

f = open(time.strftime("%Y%m%d-%H%M%S")+'_GSPData.txt','w')

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

print 'GPStime utc\t\t\tlatitude\tlongitude in view' # '\t' = TAB to try and output the data in columns.

f.write("GPStime utc, latitude, longitude in view\n")

try:
    
    while True:
        report = gpsd.next() #
        if report['class'] == 'TPV':
            GPStime =  str(getattr(report,'time',''))
            lat = str(getattr(report,'lat',0.0))
            lon = str(getattr(report,'lon',0.0))
            #speed =  str(getattr(report,'speed','nan'))
            #sats = str(len(gpsd.satellites))

            print  GPStime,"\t",
            print  lat,"\t",
            print  lon,"\t",
            #print  speed,"\t",
            #print  sats,"\t"

            f.write(GPStime + ', ' + lat +', ' + lon + '\n')
            
            #time.sleep(1)
            break
except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "Done.\nExiting."
    f.close()
