import cv2
import numpy as np

im1=cv2.imread("21.jpg")
im2=cv2.imread("23.jpg")

difference=cv2.subtract(im1,im2)

result=not np.any(difference)

if result is True:
    print "The images are the same"
else:
    print "the image are different"
