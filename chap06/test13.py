import numpy as np

arr=np.array([[99,93,60], [98,82,93], [93,65, 81], [78, 82, 81]])
print(arr, '\n')

print(np.mean(arr, axis=0))
print(arr.mean(axis=0), '\n')

print(np.mean(arr, axis=1))
print(arr.mean(axis=1))