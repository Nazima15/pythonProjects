import numpy as np

lst=[[177,77.1],
     [183, 80.1],
     [185, 78.3],
     [173, 80.3]]

arr=np.array(lst)
print('몸무개가 80 이상인 사람')
condition=arr[:,1]>=80
print(arr[condition])

print('키가 180 이상인 사람')
condition=arr[:,0]>=180
print(arr[condition][:,1])