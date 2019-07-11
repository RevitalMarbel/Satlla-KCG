import cv2

_name='/Users/revital/Pictures/earth/iss-gallery-26.jpg'

#print(frame)

#this function returns 0,1,2 : 0 - stars picture , 1- earth, curve 2- notsure
def main(name= _name):
    frame = cv2.imread(name)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    imgheight, imgwidth = frame.shape[:2]
    size=imgheight*imgwidth
    #imgwidth, imgheight = frame.shape[,:]
    dark=0
    light=0
    for i in range(0,imgheight):
            for j in range(0,imgwidth):
                if(frame[i][j]<10):
                    dark=dark+1
                if(frame[i][j]>250):
                    light=light+1
    return dark/size, light/size

print(main())