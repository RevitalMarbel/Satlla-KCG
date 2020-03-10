# import the necessary packages
import numpy as np
import argparse
import cv2
# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image file")
#ap.add_argument("-r", "--radius", type = int,
	#help = "radius of Gaussian blur; must be odd")
#args = vars(ap.parse_args())
# load the image and convert it to grayscale
image = cv2.imread("efs1.jpg")
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
cv2.circle(image, maxLoc, 10, (255, 0, 0), 2)
# display the results of the naive attempt
cv2.imshow("Naive", image)
#cv2.imshow("Robust", image)
cv2.waitKey(0)