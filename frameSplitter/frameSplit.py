import cv2
import pytesseract
from PIL import Image
import time

png_compression=50

#the name of the picture here
_name="/Users/revital/Downloads/ex3_20180618233041.jpg"



def crop( height, width, k=0,name=_name):
    path = "/temp/"+name
    frame = cv2.imread(name)
    imgheight, imgwidth = frame.shape[:2]

    k=0
    for i in range(0,imgheight,height):
        for j in range(0,imgwidth,width):
            box = (j, i, j+width, i+height)
            #a = frame[j:j+width,i: i+height]
            a = frame[i: i + height,j:j + width]
            #a.save("%s IMG-%s.png" % name %k)
            l=str(k)

            cv2.imwrite(path+"/IMG_%d.jpg" %k, a, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compression])
            #cv2.imwrite(path+"IMG_%d.png"  %k ,a)
            #cv2.imwrite(path+'IMG_%d' %k,result)
            #r = cv2.imread("IMG_%d.png" % k)
            #r=Image.open("IMG_%d.png" % k, mode='r')
            #print (r)
            #result = pytesseract.image_to_string(r)
            k +=1

def main(n):
    crop( 240,320, name=n)