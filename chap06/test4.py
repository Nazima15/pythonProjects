import numpy as np

arr=np.array([[1, 2, 3],[4, 5, 6 ]])

larr=arr[:,0]%2==0
print(arr[:,0], larr)

print(arr[larr])