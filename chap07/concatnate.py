import numpy as np
arr1=np.arange(8).reshape(2,4)
arr2=np.arange(8,16).reshape(2,4)
print(arr1)
print(arr2)
print(np.concatenate((arr1,arr2),axis=0))
print(np.concatenate((arr1,arr2),axis=1))

