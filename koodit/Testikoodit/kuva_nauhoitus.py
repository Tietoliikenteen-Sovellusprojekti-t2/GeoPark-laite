#!/usr/bin/python
import picamera
import pysftp
import MySQLdb
import os.path
import time
from gps import *
from subprocess import call

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

myHostname = "172.20.240.52"
myUsername = "ubuntu"
myPassword = "antenni2"

polku_local = "/home/pi/Photos/"
polku_server = "/home/ubuntu/pi_photos/"
kuva_nro = 1
kuva_nimi = "my_photo%d" %(kuva_nro)
kuva_form = ".jpg"
kuva_koko = polku_local + kuva_nimi + kuva_form

lat = 0.0
lon = 0.0

def nimiMuunnin (kuva_nimi, kuva_koko, kuva_nro, video_form):
    while os.path.isfile(kuva_koko):
        kuva_nimi = "my_photo%d" %(kuva_nro)
        kuva_nro += 1
        kuva_koko = polku_local + kuva_nimi + kuva_form
        print kuva_nimi
    return kuva_nimi

def kamera ():
    camera = picamera.PiCamera()
    camera.resolution = (1024, 768)
    # report = gpsd.next()
        # if report['class'] == 'TPV':
            # lat = str(getattr(report,'lat',0.0))
            # lon = str(getattr(report,'lon',0.0))
    global lat
    global lon
    lat = str(0.0)
    lon = str(0.0)
    camera.start_preview()
    time.sleep(2)
    camera.capture('%s%s%s' %(polku_local, kuva_nimi, kuva_form))


def ftp (myHostname, myUsername, myPassword):
    with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:      #ftp-blokki
        print "Connection succesfully stablished ... "

        # Define the file that you want to upload from your local directorty
        # or absolute "C:\Users\sdkca\Desktop\TUTORIAL2.txt"
        localFilePath = polku_local + kuva_nimi + kuva_form

        # Define the remote path where the file will be uploaded
        remoteFilePath = polku_server + kuva_nimi + kuva_form
        print remoteFilePath
        print localFilePath

        sftp.put(localFilePath, remoteFilePath)     # connection closed automatically at the end of the with-block

def sql (polku_server, kuva_nimi, kuva_form, aika, lat, lon):
    db = MySQLdb.connect("stulinux52.ipt.oamk.fi", "ubuntu", "antenni2", "GeoPark")
    cursor = db.cursor()
    sql1 = "insert into Kuvat(Polku, Nimi, Aikaleima) values('%s', '%s', '%s');" % ((polku_server + kuva_nimi + kuva_form), (kuva_nimi + kuva_form), aika)
    sql2 = "insert into GPS (Aikaleima, Lattitude, Longitude) values('%s', '%s', '%s');" % (aika, lat, lon)
    print sql1
    print sql2
    cursor.execute(sql1)
    cursor.execute(sql2)
    db.commit()
    db.close()
    print "Merkinta lisatty tietokantaan"

kuva_nimi = nimiMuunnin(kuva_nimi, kuva_koko, kuva_nro, kuva_form)
kamera()
aika = time.strftime("%Y%m%d%H%M")
ftp(myHostname, myUsername, myPassword)
sql(polku_server, kuva_nimi, kuva_form, aika, lat, lon)
