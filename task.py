import picamera
from time import sleep
from subprocess import call

# camera instance created from PiCamera class
camera = picamera.PiCamera()

for i in range(10):
    # Camera warm-up
    sleep(2)
    # Image captured as img_i.jpg
    capture.capture('img_' + str(i) + '.jpg')

call('git init', shell = True)
call('git add .', shell = True)
call('git commit -a "commiting..."', shell = True)
call('git push origin master', shell = True)

