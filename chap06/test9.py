import numpy as np

arr1=np.arange(8)
print(arr1, '\n')

arr2=arr1.reshape(2,4)
print(arr2, '\n')

print(arr2.flatten(), arr2.reshape(-1))