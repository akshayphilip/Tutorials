import cv2 as cv
import numpy as np

#create an image from numpy array

#black Image

img1=np.zeros((500,500),dtype='uint8')
print(img1)
print(img1.shape)

cv.imshow("black image",img1)

#white image
img2=np.ones((500,500),dtype='uint8')
img3=img2*255
print(img3)
print(img3.shape)
cv.imshow("White image",img3)

#Gray image
img4=np.ones((500,500),dtype='uint8')
img5=img4*150
print(img5)
print(img5.shape)
cv.imshow("Gray image",img5)


cv.waitKey(0)
cv.destroyAllWindows()
