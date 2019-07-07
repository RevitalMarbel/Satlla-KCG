import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

name="iss-gallery-26.jpg"
frame = cv2.imread(name)
orig=frame.copy()
height, width = frame.shape[:2]
center = (int(width / 2),int( height / 2))
packageSize=100
frameSize=10

sumOfPackage=int((((frameSize*2)*(frameSize*2))*3)/packageSize)
rez=[]
bufferCounter=0
new_frame=frame[center[0]-200:center[0]+200,center[1]-200:center[1]+200,:]
print("sum of packeges" ,sumOfPackage)
counter = 1

for i in range(0,frameSize*2):
    for j in range(0,frameSize*2):
        if(counter == 1):
            #rez.append('<')

            file = open('%d.txt' %bufferCounter, 'w')
            file.write(str(bufferCounter))
            #file.write(',')
            file.write(str(sumOfPackage))
            #file.write(',')

            rez.append(bufferCounter)
            rez.append(sumOfPackage)
            bufferCounter = bufferCounter + 1

        if(counter <packageSize-3):
            file.write(str(new_frame[i][j][0]))
            #file.write(',')
            file.write(str(new_frame[i][j][1]))
            #file.write(',')
            file.write(str(new_frame[i][j][2]))
            #file.write(',')


            rez.append(new_frame[i][j][0])
            rez.append(new_frame[i][j][1])
            rez.append(new_frame[i][j][2])

            counter=counter+3
        if (counter == packageSize-3 or (i==frameSize*2-1 and j==frameSize*2-1)):
            print(counter)
            counter = 1
            file.close()
            #rez.append('>')

# file = open('rez.txt', 'w')
#
# file.write(str(rez))
# file.close()


# print(new_frame)
# def frame_to_mat(new_frame):
#     {
#
#     }