import numpy as np

#1D SLICING

arr1=np.arange(10,101,10)

print(arr1)

arr2=arr1[1:6]
print(arr2)

arr3=arr1[1:6:2]
print(arr3)

arr4=arr1[:5]
print(arr4)

arr5=arr1[3:]
print(arr5)

arr6=arr1[-9:-2]
print(arr6)

arr7=arr1[::3]
print(arr7)

arr8=arr1[2::3]
print(arr8)

#2D SLICING

arr10=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
arr11=arr10[2,0:3]
print(arr11)

print(arr10[1:3,0:20])