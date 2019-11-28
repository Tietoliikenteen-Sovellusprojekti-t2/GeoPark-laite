import picamera
from subprocess import call

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.start_recording('my_video.h264')
camera.wait_recording(10)
camera.stop_recording()

command = "MP4Box -add my_video.h264 my_video.mp4"
call([command], shell=True)
print("vid conv")
