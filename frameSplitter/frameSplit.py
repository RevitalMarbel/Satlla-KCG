import cv2
import pytesseract
from PIL import Image
import time
path="/Users/revital/PycharmProjects/earth_curve/image_orig/"
#the name of the picture here
name="iss-gallery-26.jpg"

def crop(name, height, width, k=0):
    frame = cv2.imread(name)
    imgheight, imgwidth = frame.shape[:2]
    #imgwidth, imgheight = frame.shape[,:]
    k=0
    for i in range(0,imgheight,height):
        for j in range(0,imgwidth,width):
            box = (j, i, j+width, i+height)
            #a = frame[j:j+width,i: i+height]
            a = frame[i: i + height,j:j + width]
            #a.save("%s IMG-%s.png" % name %k)
            l=str(k)
            cv2.imwrite(path+"IMG_%d.png"  %k ,a)
            #r = cv2.imread("IMG_%d.png" % k)
            #r=Image.open("IMG_%d.png" % k, mode='r')
            #print (r)
            #result = pytesseract.image_to_string(r)
            k +=1

crop(name, 100,200)