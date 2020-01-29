import os
import cv2
import math

import base64

from pathlib import Path
import numpy as np


def main(name,path='', camera=0):
    light_threshold=0.0001
    curve_dark_threshhold=0.5
    stars_dark_threshhold = 0.8

    #tate a picture
    #cahnge to: /pic/name
    #name_jpg='/pic/'+name+'.jpg'

    #os.system('raspistill -o -cs {} {}'.format(camera,name_jpg) )
    frame=cv2.imread(path+'pic/'+name)
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #get dark and light pixles:
    dark, light=dark_light(frame)
    qual= quality(frame)
    b_qual= int_to_bytes(qual)
    print('quality', qual)


    #compress to jpeg- get size:
    png_compression=50

    #change name- to /yadayada/name
    cv2.imwrite(path+'yada_yada/'+name, frame,[int(cv2.IMWRITE_PNG_COMPRESSION), png_compression])
    statinfo = os.stat(path+'yada_yada/'+name)
    size=int(statinfo.st_size/1000)
    b_size=int_to_bytes(size)
    print ('size', size)

    #classify the frame: 1- earth curve, 2- stars, 3-sun 0- unknown
    classify=0
    if(dark<curve_dark_threshhold):
        classify=1
    if (dark > stars_dark_threshhold):
        classify = 2
    if(light> light_threshold):
        classify=3
    b_classify=int_to_bytes(classify)
    print('classify:' ,classify)

    b_dark = float_to_int(dark, 1)
    b_dark = int_to_bytes(b_dark)

    b_light = float_to_int(light, 1)
    b_light = int_to_bytes(b_light)
    print('dark', dark,'light', light)

    #turn name to bytes:
    name=1
    b_name=int_to_bytes(int(name))
    #write file discriptor:
    #chamge to /to_send/name/
    file = open(str(0)+'.txt', "wb")
    print(b_name, b_dark, b_light,  b_qual, b_size,b_classify)
    file.write(b_dark)

    file.write(b_light)

    file.write(b_qual)

    file.write(b_size)

    file.write(b_classify)
    file.close()
    os.system('cd temp &&  mkdir {}'.format(name))
    crop(320, 180, name=name,path=path, frame=frame)
    images_to_file(name=name,path=path, type=1)

    #split frame

  #  if(dark<1):
  #    os.system('mkdir /temp/name')
   #   frameSplitter.frameSplit.main(name)
   #   frameSplitter.image_to_file.main(name)

#this function gets the frame - not the name
def dark_light(frame):
    imgheight, imgwidth = frame.shape[:2]
    size = imgheight * imgwidth
    dark = 0
    light = 0
    for i in range(0, imgheight):
        for j in range(0, imgwidth):
            if (frame[i][j] < 5):
                dark = dark + 1
            if (frame[i][j] > 250):
                light = light + 1
    #print(dark, light)
    dark=dark/size
    light=light/size

    return dark,light

def quality(image):
    imgheight, imgwidth = image.shape[:2]

    # (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    # sobelx = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=11)
    # sobelx=sobelx*255
    edges = cv2.Canny(image, 80, 250)
    quality=edges.sum() / 255 / (imgheight * imgwidth)
    if(quality>0.1):
        quality=255
    else:
        quality=quality*1000
        quality=int(quality)
        #print(quality)

    #print (quality)

    #print(np.max(edges))
    #print(edges.sum() / 255) #/ (imgheight * imgwidth))
    return quality


def crop( height, width,frame,name, path, k=0):
    path = path+'temp/'+str(name)
    #frame = cv2.imread(name)
    imgheight, imgwidth = frame.shape[:2]

    k=1
    for i in range(0,imgheight,height):
        for j in range(0,imgwidth,width):
            box = (j, i, j+width, i+height)
            #a = frame[j:j+width,i: i+height]
            a = frame[i: i + height,j:j + width]
            #a.save("%s IMG-%s.png" % name %k)
            l=str(k)
            png_compression=50
            #cv2.imwrite(path+'/%d.jpg' %k, a, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compression])
            cv2.imwrite( path+'temp/'+str(name)+'/%d.jpg'  %k, a, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compression])
            #cv2.imwrite(path+"IMG_%d.png"  %k ,a)
            #cv2.imwrite(path+'IMG_%d' %k,result)
            #r = cv2.imread("IMG_%d.png" % k)
            #r=Image.open("IMG_%d.png" % k, mode='r')
            #print (r)
            #result = pytesseract.image_to_string(r)
            k +=1

def images_to_file(name,path, type ):
    path=path+'/temp/'+str(name)+'/'
    entries = Path(path)
    if(type):
        counter=1
        os.system('cd to_send &&  mkdir {}'.format(name))
        for entry in entries.iterdir():
            #if('IMG_' in entry.name):
                #print(entry.name)
                file = open( path+'/'+entry.name ,'rb')
                #print(file.read())
                result = base64.b64encode(file.read())
                #print(result  )
                file = open('/to_send/'+name+'/%s.txt' % counter, 'wb')
                file.write(result)
                file.close()
                counter=counter+1
        #file = open('/to_send/name/%s.txt' % str(0), 'wb')
        #file.write(name, counter, type, time ,br )
        #file.close()

def pixel_normallize(pix, width,heigh):
    res_x=pix[0]/width
    res_y=pix[1]/heigh
    return [res_x,res_y]


#pixel is adecimal number smaller than 1
def pixel_to_int(pix):
    pix[0]= pix[0]* math.pow(2,16)
    pix[1] = pix[1] * math.pow(2,16)
    pix[0]= int(pix[0])
    pix[1] = int(pix[1])
    return pix


def float_to_int(f, b_num):
    f = f * math.pow(2, 8*b_num)
    f=int(f)
    return f

#byte compression
def int_to_pixel(i_x):
    i_x[0] = i_x[0]/(math.pow(2,16))
    i_x[1]=  i_x[1]/(math.pow(2,16))
    return i_x


def int_to_bytes_touple(x):
    return [int_to_bytes(x[0]),int_to_bytes(x[1])]

def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes_touple(x):
    return [int_from_bytes(x[0]),int_from_bytes(x[1])]

def int_from_bytes(xbytes: bytes):
    return int.from_bytes(xbytes, 'big')

main(path='/Users/revital/PycharmProjects/Satlla-KCG/',name='1.jpg')