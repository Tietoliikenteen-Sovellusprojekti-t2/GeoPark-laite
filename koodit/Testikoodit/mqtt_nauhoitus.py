#!/usr/bin/python
import paho.mqtt.client as mqtt
import picamera
import pysftp
import MySQLdb
import os.path
import time
import keyboard
import paho.mqtt.client as mqtt
from subprocess import call
#import pynput
#from pynput.keyboard import Key, Controller

myHostname = "172.20.240.52"
myUsername = "ubuntu"
myPassword = "antenni2"

polku_local = "/home/pi/Videos/"
polku_server = "/home/ubuntu/pi_video/"
video_nro = 1
video_nimi = "my_video%d" %(video_nro)
video_form = ".mp4"
video_koko = polku_local + video_nimi + video_form

camera = picamera.PiCamera()
stream = picamera.PiCameraCircularIO(camera, seconds=40)

muuttuja1 = 0
muuttuja2 = 0

#keyboard = Controller()

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("test")
	client.subscribe("topic")

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
    	global muuttuja1
	global muuttuja2
	if msg.payload == "vsave":
		print "Received VIDEO SAVE message!"
		#os.system("python /home/pi/GeoPark-laite/koodit/Testikoodit/TiedonLisaysTietokantaan_v1.py")
        	muuttuja1 = 1
        	print muuttuja1
#		keyboard.press('a')
#		keyboard.release('a')
	if msg.payload == "vstop":
		print "Received VIDEO STOP message!"
		muuttuja2 = 1
#		keyboard.press('b')
#                keyboard.release('b')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("172.20.240.52")
client.loop_start()

def nimiMuunnin (video_nimi, video_koko, video_nro, video_form):
    while os.path.isfile(video_koko):                                                   
        video_nimi = "my_video%d" %(video_nro)                                
        video_nro += 1                                                        
        video_koko = polku_local + video_nimi + video_form                    
        print video_nimi
    return video_nimi                                                         
        
def  kamera ():
    camera.start_recording(stream, format='h264')
    try:
        while True:
            camera.wait_recording(1)
            if muuttuja2 == 1:
		camera.stop_recording()
		client.loop_stop()
                exit()
            else:
                if muuttuja1 == 1:
                    print "painoit NAPPULAAA :DD"
                    # Keep recording for 10 seconds and only then write the
                    # stream to disk
                    camera.wait_recording(5)
                    stream.copy_to('%s%s.h264' %(polku_local, video_nimi), seconds = 10)
                    break
    finally:
        camera.stop_recording()

def kaantaja ():
    command = "MP4Box -add %s%s.h264 %s%s.mp4" %(polku_local, video_nimi, polku_local, video_nimi)
    call([command], shell=True)
    print("vid conv")

def ftp (myHostname, myUsername, myPassword):
    with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:      #ftp-blokki
        print "Connection succesfully stablished ... "
        
        # Define the file that you want to upload from your local directorty
        # or absolute "C:\Users\sdkca\Desktop\TUTORIAL2.txt"
        localFilePath = polku_local + video_nimi + video_form

        # Define the remote path where the file will be uploaded
        remoteFilePath = polku_server + video_nimi + video_form
        print remoteFilePath
        print localFilePath

        sftp.put(localFilePath, remoteFilePath)     # connection closed automatically at the end of the with-block

def sql (polku_server, video_nimi, video_form, aika):
    db = MySQLdb.connect("stulinux52.ipt.oamk.fi", "ubuntu", "antenni2", "GeoPark")
    cursor = db.cursor()
    sql = "insert into Videot(Polku, Nimi, Aikaleima) values('%s', '%s', '%s');" % ((polku_server + video_nimi + video_form), (video_nimi + video_form), aika)
    print sql
    cursor.execute(sql)
    db.commit()
    db.close()
    print "Merkinta lisatty tietokantaan"    
    global muuttuja1
    global muuttuja2
    muuttuja1 = 0
    muuttuja2 = 0

while True:
    video_nimi = nimiMuunnin(video_nimi, video_koko, video_nro, video_form)
    kamera()
    aika = time.strftime("%Y%m%d%H%M%S")
    kaantaja()
    ftp(myHostname, myUsername, myPassword)
    sql(polku_server, video_nimi, video_form, aika)
