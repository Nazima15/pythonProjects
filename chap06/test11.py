import numpy as np

np.random.seed(1)
print(np.random.normal(0,1,5))

np.random.seed(1)
print(np.random.randn(5))
print()

np.random.seed(1)
print(np.random.normal(10,2,(22,5)))
print()

np.random.seed(1)
print(np.random.randn(2,5)*2+10)