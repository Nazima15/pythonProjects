import numpy as np

arr=np.array([[1, 2, 3],[4, 5, 6]])
larr=arr%2==0
print(larr)

print(arr[larr])