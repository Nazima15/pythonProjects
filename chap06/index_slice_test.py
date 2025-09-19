import numpy as np

arr=np.array([1,2,3,4,5])
n=arr.size

print(arr[0])
print(arr[-1],arr[n-1])

print(arr[1:4])
print(arr[0:-1], arr[0:4])
print(arr[:],arr[0:],arr[:n],arr[0:n])