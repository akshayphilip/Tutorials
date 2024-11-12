#1D array indexing

import numpy as np
arr1=np.arange(10,101,10)
print(arr1)

index=arr1[3]
print(index)

index1=arr1[-7]
print(index1)


#2D array Indexing
arr2=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
index2=arr2[2,1]
print(index2)

#3D array index

arr3=np.array([
    [[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
    [[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
    [[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
    ])


index3=arr3[0,2,2]
print(index3)