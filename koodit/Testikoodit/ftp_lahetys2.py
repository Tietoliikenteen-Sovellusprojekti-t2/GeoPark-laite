import pysftp

myHostname = "172.20.240.52"
myUsername = "ubuntu"
myPassword = "antenni2"

class polku:
    def __init__(tieto, polku, nimi):
    	tieto.polku = polku
    	tieto.nimi = nimi
    
    def paikallinen(tieto):
        localFilePath =  tieto.polku + tieto.nimi

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print "Connection succesfully stablished ... "

    p1 = polku('/home/pi/', 'pivideo.mp4')
    p1.paikallinen()
    # Define the file that you want to upload from your local directorty
    # or absolute "C:\Users\sdkca\Desktop\TUTORIAL2.txt"
    #localFilePath = './TUTORIAL2.txt'

    # Define the remote path where the file will be uploaded
    remoteFilePath = '/var/integraweb-db-backups/TUTORIAL2.txt'

    sftp.put(p1.paikallinen(), remoteFilePath)
 
# connection closed automatically at the end of the with-block
