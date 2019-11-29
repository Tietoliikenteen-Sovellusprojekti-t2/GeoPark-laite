import picamera
import pysftp
import MySQLdb
import os.path
from subprocess import call

myHostname = "172.20.240.52"
myUsername = "ubuntu"
myPassword = "antenni2"

polku_local = "/home/pi/GeoPark-laite/koodit/Testikoodit/"
polku_server = "/home/ubuntu/"
video_nro = 1
video_nimi = "my_video%d" %(video_nro)
video_form = ".mp4"
video_koko = polku_local + video_nimi + video_form
testi4 = "30"

def nimiMuunnin (video_nro, video_koko, video_nimi, video_form, polku_local):
    while os.path.isfile(video_koko):
        video_nimi = "my_video%d" %(video_nro)
        video_nro += 1
        video_koko = polku_local + video_nimi + video_form
        #print video_nimi
    return video_nimi
        
video_nimi = nimiMuunnin(video_nro, video_koko, video_nimi, video_form, polku_local)

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.start_recording('%s.h264' %video_nimi)
camera.wait_recording(10)
camera.stop_recording()

command = "MP4Box -add %s.h264 %s.mp4" %(video_nimi, video_nimi)
call([command], shell=True)
print("vid conv")

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
 


db = MySQLdb.connect("stulinux52.ipt.oamk.fi", "ubuntu", "antenni2", "GeoPark")

cursor = db.cursor()
sql = "insert into Videot(Polku, Nimi, Aikaleima) values('%s', '%s', '%s');" % ((polku_server + video_nimi + video_form), (video_nimi + video_form), testi4)
print sql
cursor.execute(sql)
db.commit()
db.close()
print "Merkinta lisatty tietokantaan"
