from picamera import PiCamera
from time import sleep
from datetime import datetime
date=datetime.now()
date=date.strftime('%Y%m%d%H%M%S')

camera = PiCamera()
camera.rotation=180
camera.start_preview(alpha=200)
sleep(5)
camera.capture('%s.jpg' %date)
camera.stop_preview()
