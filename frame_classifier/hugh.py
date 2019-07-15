import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

cap = cv2.VideoCapture('iss_earth.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
threshhold= 10
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

#inputImage = cv2.imread("images-9.jpeg")
    height, width = frame.shape[:2]
    inputImageGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(inputImageGray, (5, 5), 0)
    edges = cv2.Canny(blurred,20,100,apertureSize = 3)
    minLineLength = 0
    maxLineGap = 0
    #lines = cv2.HoughLinesP(edges,cv2.HOUGH_PROBABILISTIC, np.pi/270, 1, minLineLength,maxLineGap)
    curve_x=[]
    curve_y=[]

    #np.transpose(edges)
    edges= edges.T
    distortion=0
    for j in range(0,len(edges)-1):
        i=0
        while(i< len(edges[j]) and edges[j][i] !=255 ):
            i=i+1

        curve_x.append(j)
        curve_y.append(i)
        pts = np.array([[j, i], [j, i]], np.int32)
        cv2.polylines(frame, [pts], True, (0, 255, 0))
    for y in curve_y:
        distortion=distortion+math.abs(y- curve_y.mean())
    print(distortion)




        #print(i,j)
    #s = interpolate.interp1d(curve_x, curve_y)

    #polynomial_features = PolynomialFeatures(degree=2)
    #x_poly = polynomial_features.fit_transform([curve_x,curve_y])

    #print(x_poly)
    #print (s)
    #xnew = np.arange(0, width-1)
    #ynew=interpolate.splev(xnew, s, der=0)

    #print(np.poly(curve_y))
    #ynew=s(xnew)

    #plt.figure()
    #plt.plot(curve_x, curve_y, 'x', xnew, ynew, 'b')
    #plt.legend(['curve', 'InterpolatedUnivariateSpline'])
    #plt.axis([-0.05, 6.33, -1.05, 1.05])
    #plt.title('InterpolatedUnivariateSpline')
    #plt.show()

    # for x in range(0, len(lines)):
    #     for x1,y1,x2,y2 in lines[x]:
    #         #cv2.line(inputImage,(x1,y1),(x2,y2),(0,128,0),2, cv2.LINE_AA)
    #         pts = np.array([[x1, y1 ], [x2 , y2]], np.int32)
    #         cv2.polylines(inputImage, [pts], True, (0,255,0))
    #         #print(pts)
    #         #print(pts[:,0], pts[1,:])
    #         if(len(pts)>5):



    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,"Tracks Detected", (500, 250), font, 0.5, 255)
    out.write(frame)
    cv2.imshow("Trolley_Problem_Result", frame)
    #cv2.imshow('edge', edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        out.release()
        break

    #cv2.waitKey(0)
cap.release()
out.release()
cv2.destroyAllWindows()
