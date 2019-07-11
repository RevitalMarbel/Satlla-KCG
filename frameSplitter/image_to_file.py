
import base64

from pathlib import Path


def main(name, type, time=0,br=0 ):
    path='/temp/'+name
    entries = Path(path)


    counter=1
    for entry in entries.iterdir():
        #if('IMG_' in entry.name):
            #print(entry.name)
            file = open( path+'/'+entry.name ,'rb')
            #print(file.read())
            result = base64.b64encode(file.read())
            #print(result  )
            file = open('/to_send/name/%s.txt' % counter, 'wb')
            file.write(result)
            file.close()
            counter=counter+1
    file = open('/to_send/name/%s.txt' % str(0), 'wb')
    file.write(name, counter, type, time ,br )
    file.close()