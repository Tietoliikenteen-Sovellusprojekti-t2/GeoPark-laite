import pysftp

myHostname = "172.20.240.52"
myUsername = "ubuntu"
myPassword = "antenni2"

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print "Connection succesfully stablished ... "
    #testi = sftp.getcwd
    testi2 = '/home/pi/'
    testi3 = 'pivideo.mp4'
    #print testi
    # Define the file that you want to upload from your local directorty
    # or absolute "C:\Users\sdkca\Desktop\TUTORIAL2.txt"
    localFilePath = testi2 + testi3

    # Define the remote path where the file will be uploaded
    remoteFilePath = '/home/ubuntu/pivideo.mp4'

    sftp.put(localFilePath, remoteFilePath)
 
# connection closed automatically at the end of the with-block
