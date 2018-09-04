import cv2
import numpy as np



im11=cv2.imread("21.jpg")
im1=im11[1:250, 1:250]
for i in range(1,100000):
    z="%d.jpg"%(i)
    im21=cv2.imread(z)
    im2=im21[1:250, 1:250]
    
    difference=cv2.subtract(im1,im2)

    result=not np.any(difference)

    if result is True:
        print z
        break

