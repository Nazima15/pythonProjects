import numpy as np

arr=np.array([1, 2, 3, 4, 5])
print(arr[[0,2,4]])
larr=arr>=3
print(larr)
print(arr[larr])