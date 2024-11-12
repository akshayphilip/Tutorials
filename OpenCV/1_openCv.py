import cv2 as cv
#Read,Display & Save an image


img =cv.imread('bird3.jpeg')

cv.imshow("Image",img)

cv.imwrite('new.jpg',img)

cv.waitKey(0)
cv.destroyAllWindows() 
