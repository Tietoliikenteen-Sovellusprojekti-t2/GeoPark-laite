import pysftp

myHostname = "172.20.240.52"
myUsername = "ubuntu"
myPassword = "antenni2"

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print "Connection succesfully stablished ... "

    # Define the file that you want to download from the remote directory
    remoteFilePath = '/home/ubuntu/testi.txt'

    # Define the local path where the file will be saved
    # or absolute "C:\Users\sdkca\Desktop\TUTORIAL.txt"
    localFilePath = '/home/pi/testi.txt'

    sftp.get(remoteFilePath, localFilePath)
 
# connection closed automatically at the end of the with-block