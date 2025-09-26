import numpy as np

arr=np.array([50, 60, 70, 80, 90])
condition=arr>=80
print(condition)
passed=arr[condition]
print(passed)