import picamera
import time
import datetime

savepath = '/home/pi/Desktop/BlackBox'

def recordTenSeconds():
    with picamera.PiCamera() as camera:
        camera.resolution = (640,480)
        now = datetime.datetime.now()
        filename = now.strftime('%d-%H:%M:%S')
        camera.start_recording(output = savepath + '/' + filename + '.h264')
        camera.start_preview()
        camera.wait_recording(60)
        camera.stop_preview()
        camera.stop_recording()
