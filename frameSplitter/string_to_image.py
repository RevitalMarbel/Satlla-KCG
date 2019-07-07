import base64

from pathlib import Path
path='/Users/revital/PycharmProjects/earth_curve/txt_res'
entries = Path(path)
for entry in entries.iterdir():
    if('tfi' in entry.name):
        print(entry.name)
        image_file = open(path+'/'+entry.name, 'rb')
        r=image_file.read()
        r=base64.b64decode(r)
        #r=r.decode('base64')
        print(r)
        fh = open("Image_res/ImageFromFile_%s.png" % entry.name, "wb")
        fh.write(r)
        fh.close()


