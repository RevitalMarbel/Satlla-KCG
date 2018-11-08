import os
os.system('command')
for i in range (40,60):
    os.system('raspistill -o gaza%d.jpg' %(i))
