from picamera import PiCamera
from time import sleep
from datetime import datetime
from fractions import Fraction
date=datetime.now()
tempdate=date.strftime('%Y%m%d%H%M%S')

camera = PiCamera()
#camera.resolution=(1280,720)
camera.framerate=Fraction(1,6)
camera.brightness=80
#camera.framerate=100
camera.rotation=180

camera.iso=800
camera.shutter_speed=2000000
camera.exposure_mode='off'
#camera.start_preview(alpha=200)
for i in range(20):
    sleep(10)
    date=datetime.now()
    tempdate=date.strftime('%Y%m%d%H%M%S')
    camera.capture('ex2_%s.jpg' %tempdate )
#camera.stop_preview()
