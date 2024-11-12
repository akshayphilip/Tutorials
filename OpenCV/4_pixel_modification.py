import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#acessing an  modifying pixel values
img= cv.imread('bird3.jpeg')

#printing the pixel value
#px=img[100,100]
#print(px)

#change the pixel value of the selected region
#img[40:80,50:150]= (255,0,0)

#cuting the selcted pixel region
img1=img[40:80,50:150]
cv.imshow('image1',img1)

cv.imshow('image',img)

print(img.shape)
plt.imshow(img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows() 