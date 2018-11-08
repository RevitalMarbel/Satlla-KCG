import numpy as np
import argparse
import cv2
from picamera import PiCamera
from time import sleep
from datetime import datetime
date=datetime.now()
date=date.strftime('%Y%m%d%H%M%S')

camera = PiCamera()
camera.capture('%s.jpg' %date)


# if you want to read from CMD
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image file")
#args = vars(ap.parse_args())
#image = cv2.imread('fullExStarS9.jpg')

#file_name="fullExStarS9.jpg"

file_name='%s.jpg' %date

file = open("%s_res.txt" %file_name  ,"w")
image = cv2.imread(file_name)
orig = image.copy()
image = image[0:2000,0:4025 ]

#orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

edges = cv2.Canny(image, 100, 200)
#cv2.circle(edges, maxLoc, 5, (255, 0, 0), 3)
_, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour_list = []
for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    area = cv2.contourArea(contour)
    (x, y), radius = cv2.minEnclosingCircle(contour)
    center = (int(x), int(y))
    radius = int(radius)
    x=center[0]
    y =center[1]
    x=str(x)
    y = str(y)
    r =str(radius)

    file.write("%s ,%s ,%s" % (x ,y , r))
    #file.write(t)
    file.write('\n')
    if (radius >0):
        cv2.circle(orig, center, radius+10, (0, 255, 255), 5)
    #if ((len(approx) > 8) & (len(approx) < 23) & (area > 30) ):
    contour_list.append(contour)
#ret, thresh = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
connectivity = 4
#output = cv2.connectedComponentsWithStats(image, connectivity, cv2.CV_32S)
#cv2.drawContours(image, contour_list,  -1, (255,255,0), 1)
# display the results of the naive attempt

#cv2.imshow("Naive", orig)
cv2.imwrite("processed%s.jpg" % file_name, orig)
cv2.waitKey(0)
file.close()
