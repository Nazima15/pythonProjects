import matplotlib.pyplot as plt
import numpy as np

x=np.arange(20,50)
y=x+2*np.random.randn(30)

plt.scatter(x, y)
plt.title('Real Age vs Phisical Age')
plt.xlabel('Real Age')
plt.ylabel('Phisical Age')

plt.savefig("kkk.png", dpi=600)
plt.show()