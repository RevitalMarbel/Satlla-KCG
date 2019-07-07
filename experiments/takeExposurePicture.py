import os
from datetime import datetime
date=datetime.now()
date=date.strftime('%Y%m%d%H%M%S')
os.system('raspistill -vf -hf -o %s.jpg' %date)