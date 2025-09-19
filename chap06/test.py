import numpy as np

arr1=np.array([1,2,3])
print(arr1)
print(arr1.ndim, arr1.shape, arr1.dtype, arr1.itemsize, arr1.size)

arr2=np.array([[1,2,3], [4,5,6]])
print(arr2)
print(arr2.ndim, arr2.shape, arr2.dtype, arr2.itemsize, arr2.size)

arr3=np.array([[[1,1,1],[2,2,2]],[[3,3,3], [4,4,4]]])
print(arr3)
print(arr3.ndim, arr3.shape, arr3.dtype, arr3.itemsize, arr3.size)
