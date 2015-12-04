import picamera
from time import sleep

# camera instance created from PiCamera class
camera = picamera.PiCamera()

for i in range(10):
    # Camera warm-up
    sleep(2)
    # Image captured as img_i.jpg
    capture.capture('img_' + str(i) + '.jpg')
