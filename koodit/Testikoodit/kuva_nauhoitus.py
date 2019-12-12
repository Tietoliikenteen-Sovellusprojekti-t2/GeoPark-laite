#!/usr/bin/python
# import paho.mqtt.client as mqtt
import picamera
import pysftp
import MySQLdb
import os.path
import time
# import keyboard
# import paho.mqtt.client as mqtt
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

camera = picamera.PiCamera()
camera.resolution = (1024, 768)

# muuttuja1 = 0
# muuttuja2 = 0

#keyboard = Controller()

# def on_connect(client, userdata, flags, rc):
	# print("Connected with result code "+str(rc))
	# client.subscribe("test")
	# client.subscribe("topic")

# def on_message(client, userdata, msg):
	# print(msg.topic+" "+str(msg.payload))
    	# global muuttuja1
	# global muuttuja2
	# if msg.payload == "vsave":
		# print "Received VIDEO SAVE message!"
		# #os.system("python /home/pi/GeoPark-laite/koodit/Testikoodit/TiedonLisaysTietokantaan_v1.py")
        	# muuttuja1 = 1
        	# print muuttuja1
# #		keyboard.press('a')
# #		keyboard.release('a')
	# if msg.payload == "vstop":
		# print "Received VIDEO STOP message!"
		# muuttuja2 = 1
# #		keyboard.press('b')
# #                keyboard.release('b')

# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message
# client.connect("172.20.240.52")
# client.loop_start()

def nimiMuunnin (kuva_nimi, kuva_koko, kuva_nro, video_form):
    while os.path.isfile(kuva_koko):                                                   
        video_nimi = "my_photo%d" %(kuva_nro)                                
        kuva_nro += 1                                                        
        kuva_koko = polku_local + kuva_nimi + kuva_form                    
        print kuva_nimi
    return kuva_nimi                                                         
        
def  kamera ():
    # report = gpsd.next() 
        # if report['class'] == 'TPV':
            # lat = str(getattr(report,'lat',0.0))
            # lon = str(getattr(report,'lon',0.0))
    lat = str(0.0)
    lon = str(0.0)
    camera.start_preview()
    sleep(2)
    camera.capture('%s%s.%s' %(polku_local, kuva_nimi, kuva_form)

# def kaantaja ():
    # command = "MP4Box -add %s%s.h264 %s%s.mp4" %(polku_local, video_nimi, polku_local, video_nimi)
    # call([command], shell=True)
    # print("vid conv")

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

def sql (polku_server, kuva_nimi, kuva_form, aika):
    db = MySQLdb.connect("stulinux52.ipt.oamk.fi", "ubuntu", "antenni2", "GeoPark")
    cursor = db.cursor()
    sql = "insert into Kuvat(Polku, Nimi, Aikaleima) values('%s', '%s', '%s');" % ((polku_server + kuva_nimi + kuva_form), (kuva_nimi + kuva_form), aika)
    print sql
    cursor.execute(sql)
    db.commit()
    db.close()
    print "Merkinta lisatty tietokantaan"    
    # global muuttuja1
    # global muuttuja2
    # muuttuja1 = 0
    # muuttuja2 = 0

# while True:


kuva_nimi = nimiMuunnin(kuva_nimi, kuva_koko, kuva_nro, kuva_form)
kamera()
aika = time.strftime("%Y%m%d%H%M%S")
# kaantaja()
ftp(myHostname, myUsername, myPassword)
sql(polku_server, kuva_nimi, kuva_form, aika)
