import numpy as np
import argparse
import cv2


# if you want to read from CMD
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image file")
#args = vars(ap.parse_args())
#image = cv2.imread('fullExStarS9.jpg')


def takeRadius(elem):
    return elem[2]

file_name='/Users/revital/Pictures/earth/iss-gallery-26.jpg'

file = open("%s_res.txt" %file_name  ,"w")
image = cv2.imread(file_name)
orig = image.copy()
#image = image[0:2500,0:4000 ]
#orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

edges = cv2.Canny(image, 80, 200)
#print (edges)
#cv2.circle(edges, maxLoc, 5, (255, 0, 0), 3)
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#print (contours)
contour_list = []
#print (contours)
#0area = cv2.contourArea(contours[0])
res=[]
for contour in contours:
    #approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    #print("in for")
    area = cv2.contourArea(contour)
    #print(area)
    (x, y), radius = cv2.minEnclosingCircle(contour)

    center = (int(x), int(y))
    radius = int(radius)
    xint=center[0]
    yint =center[1]
    x=str(x)
    y = str(y)
    r =str(radius)


    if (radius >2): #(and xint>300 and yint> 300):
        cv2.circle(orig, center, radius, (0, 255, 255), 5)
        res.append([x, y, radius])
#contour_list.append(contour)
#ret, thresh = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
connectivity = 4
#output = cv2.connectedComponentsWithStats(image, connectivity, cv2.CV_32S)
#cv2.drawContours(image, contour_list,  -1, (255,255,0), 1)
# display the results of the naive attempt
cv2.imshow("Naive", orig)
cv2.imwrite("%s_processed.jpg" % file_name, orig)

res.sort(key=takeRadius,reverse=True )
#cv2.waitKey(0)
for i in range(0,10):
    file.write("%s ,%s ,%s" % (res[i][0] ,res[i][1] , res[i][2]))
        #file.write(t)
    file.write('\n')
file.close()