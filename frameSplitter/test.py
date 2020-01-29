import cv2
import numpy as np
from PIL import Image, ImageStat
from matplotlib import pyplot as plt
import numpy as np
from exif import Image as image

def brightness(im_file):
    im = Image.open(im_file).convert('L')
    stat = ImageStat.Stat(im)
    return stat.rms[0]


im_file ='/Users/revital/PycharmProjects/Satlla-KCG/temp/1.jpg'
b=brightness(im_file)
print ("bright" ,b)

with open('/Users/revital/PycharmProjects/Satlla-KCG/temp/1.jpg', 'rb') as image_file:
    my_image = image(image_file)
    print(my_image.brightness_value)
    #print(dir(my_image))


name='/Users/revital/Pictures/sun/CG5ZbDXVIAE1z3r'
img_e = cv2.imread(name+'.jpg',0)
laplacian = cv2.Laplacian(img_e,cv2.CV_64F)

img=my_image


sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=11)

#img = cv2.resize(img,(64,32))
#cv2.imwrite("%sresizeimg.jpg" %name ,img,[int(cv2.IMWRITE_PNG_COMPRESSION), 50])

l=np.absolute(laplacian)
#print(l)
#print(l.sum())
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=11)
#np.fft.fft2(a)
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(l,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()