import matplotlib.pyplot as plt
import numpy as np

x=[x for x in range(1000)]
y=np.random.rand(1000)*6-3

plt.figure(figsize=(12,4))
plt.title("Random Numbers")
plt.plot(x, y, 'bo-')
plt.axis((0,1000,-3.5,3.5))

plt.show()