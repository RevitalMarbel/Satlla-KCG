import cv2

import matplotlib.pyplot as plt
import numpy as np


im_file ='//Users/revital/Pictures/sun/4'

img_e = cv2.imread(im_file+'.jpg',1)
print (img_e)
orig=np.fft.fft2(img_e)
orig_abs=abs(orig)
Z_shift = np.fft.fftshift(orig)
Z_shift_abs=abs(Z_shift)
print(orig)

invers=np.fft.ifft2(Z_shift)
invers_abs=abs(img_es)


plt.subplot(2,2,1),plt.imshow(img_e, extent=[0,1,0,1])
plt.title('Original'), plt.xticks([]), plt.yticks([])
#plt.imshow(img_e, extent=[0,1,0,1])

plt.subplot(2,2,2),plt.imshow(invers_abs)
plt.title('invers'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3),plt.imshow(orig_abs)
plt.title('unshift fft'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4),plt.imshow(Z_shift_abs)
plt.title('shift'), plt.xticks([]), plt.yticks([])


plt.show()