import io
import random
import picamera

def motion_detected():
    # Randomly return True (like a fake motion detection routine)
    return random.randint(0, 3) == 0

camera = picamera.PiCamera()
stream = picamera.PiCameraCircularIO(camera, seconds=10)
camera.start_recording(stream, format='h264')
try:
    while True:
        camera.wait_recording(1)
        if motion_detected():
            # Keep recording for 10 seconds and only then write the
            # stream to disk
            camera.wait_recording(5)
            stream.copy_to('motion.h264')
finally:
    camera.stop_recording()
