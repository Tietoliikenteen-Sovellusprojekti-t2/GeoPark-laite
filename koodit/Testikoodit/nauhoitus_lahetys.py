import picamera
import pysftp
from subprocess import call

myHostname = "172.20.240.52"
myUsername = "ubuntu"
myPassword = "antenni2"

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.start_recording('my_video.h264')
camera.wait_recording(10)
camera.stop_recording()

command = "MP4Box -add my_video.h264 my_video.mp4"
call([command], shell=True)
print("vid conv")

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print "Connection succesfully stablished ... "
    #testi = sftp.getcwd
    testi2 = '/home/pi/GeoPark-laite/koodit/Testikoodit/'
    testi3 = 'my_video.mp4'
    #print testi
    # Define the file that you want to upload from your local directorty
    # or absolute "C:\Users\sdkca\Desktop\TUTORIAL2.txt"
    localFilePath = testi2 + testi3

    # Define the remote path where the file will be uploaded
    remoteFilePath = '/home/ubuntu/my_video.mp4'

    sftp.put(localFilePath, remoteFilePath)
 
# connection closed automatically at the end of the with-block
