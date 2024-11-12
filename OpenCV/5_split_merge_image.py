import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#splitinh and mergin an image
img= cv.imread('bird3.jpeg')

b,g,r=cv.split(img)

img2=cv.merge((b,g,r))
img3=cv.merge((r,g,b))

cv.imshow('image',img)

cv.imshow('blue',b)
cv.imshow('red',r)
cv.imshow('green',g)

cv.imshow('merge',img2)
cv.imshow('merge_new',img3)

cv.waitKey(0)
cv.destroyAllWindows() 