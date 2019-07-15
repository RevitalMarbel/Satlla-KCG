import cv2
import numpy as np


def takeRadius(elem):
    return elem[2]

name='/Users/revital/Pictures/sun/images-12.jpeg'
img = cv2.imread(name)

#img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#edges = cv2.Canny(gray,20,100,apertureSize = 3)
minLineLength = 100
maxLineGap = 200
#lines = cv2.HoughLinesP(edges,cv2.HOUGH_PROBABILISTIC,np.pi/180,10,minLineLength,maxLineGap)
circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT, 1, 20,param1 = 70, param2 = 30, minRadius = 10, maxRadius = 30)
print(circles[0,:])
#circles = np.uint16(np.around(circles))
#print(circles[0,:].sort(key=takeRadius,reverse=True))
for i in circles[0,:]:
        print(i)
       # draw the outer circle
        if(i[2]>10):
                cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
                cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

#cv2.imshow('detected circles',cimg)
cv2.imwrite("%s_processed_hugh.jpg" % name, cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
