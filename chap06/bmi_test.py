import numpy as np

h=[1.83, 1.75, 1.71, 1.85, 1.77, 1.73]
w=[80,74,59,90,77,78]

harr=np.array(h)
warr=np.array(w)

bmi=warr/harr**2
print(bmi)