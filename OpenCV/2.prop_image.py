import cv2 as cv

#image Properties

#binary
img=cv.imread('bird3.jpeg',0)
img2=cv.imread('bird3.jpeg',0)
img3=cv.imread('bird3.jpeg')

cv.imshow("gray scale image",img)

#type of the image
print(type(img))

#shape of the image 
print(img.shape)

#data type of the image
print(img.dtype)

#size of the image total pixel size
print(img.size)

#it will same as array
print(img)


#gray scale image

#type of the image
print(type(img2))

#shape of the image 
print(img2.shape)

#data type of the image
print(img2.dtype)

#size of the image total pixel size
print(img2.size)

#it will same as array
print(img2)

#colour image

#type of the image
print(type(img3))

#shape of the image 
print(img3.shape)

#data type of the image
print(img3.dtype)

#size of the image total pixel size
print(img3.size)

#it will same as array
print(img3)

cv.waitKey(0)
cv.destroyAllWindows()