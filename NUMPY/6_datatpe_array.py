import numpy as np

arr1=np.array([1,2,3,4,5])

#find the data type of an array
print(arr1.dtype)


arr2=np.array([1.2,2,3,4,5])
print(arr2.dtype)


arr3=np.array(["a","b","c","ds"])
print(arr3.dtype)

# Create an array with data Type

arr5=np.array([1,2,3,4,5],dtype=np.int8)

print(arr5.dtype)


#conver the data types

arr6=np.array([1,2,3,4,5],dtype=np.int8)

arr7=arr6.astype(np.float16)
print(arr7.dtype)
