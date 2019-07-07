
import base64

from pathlib import Path
path='/Users/revital/PycharmProjects/earth_curve/image_orig'
entries = Path(path)
for entry in entries.iterdir():
    if('IMG_' in entry.name):
        print(entry.name)
        file = open( path+'/'+entry.name ,'rb')
        #print(file.read())
        result = base64.b64encode(file.read())
        print(result  )
        file = open('/Users/revital/PycharmProjects/earth_curve/txt_res/%s_tfi.txt' % entry.name, 'wb')
        file.write(result)
        file.close()