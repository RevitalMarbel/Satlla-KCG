import os
from time import sleep
os.system('command')
for i in range (100,200):
    os.system('raspistill -n -t 1000 -ss 5000000 -ISO 800 -o star%d.jpg' %(i))
    sleep(120)
