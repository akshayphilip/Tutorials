import numpy as np

# 1D TO 2D Array
arr1=np.array([1,2,3,4,5,6])
print(arr1)

newarr1=arr1.reshape(2,3)
print(newarr1)


#1D to 3D array
arr2=np.array([1,2,3,4,5,6,8,9])

print(arr2)

newarr2=arr2.reshape(2,2,2)
print(newarr2)

#2D to 2d array
arr3=np.array([[1,2],[3,4],[5,6],[7,8]])

print(arr3)

newarr3= arr3.reshape(2,4)

print(newarr3)


#2D array to 3D array
arr4=np.array([[1,2],[3,4],[5,6],[7,8]])
print(arr4)

newarr4=arr4.reshape(2,2,2)
print(newarr4)

#3D to 2D Array
newarr5=newarr4.reshape(4,2)
print(newarr5)

#multidimensional array to one dimension array
print(newarr4.shape)
newarr5=newarr1.reshape(-1)

print(newarr5)
print(newarr5.shape)


