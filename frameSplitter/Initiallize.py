import frame_classifier.up_or_down
import frameSplitter
import os

def main(name):
    #rate a picture
    name_jpg='pic/name+'.jpg
    os.system('raspistill -o {}'.format(name_jpg))
    dark, light=frame_classifier.up_or_down.main(name_jpg)
    if(dark<1):
      os.system('mkdir /temp/name')
      frameSplitter.frameSplit.main(name)
      frameSplitter.image_to_file.main(name)
