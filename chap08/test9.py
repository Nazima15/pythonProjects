import pandas as pd
import numpy as np

df=pd.DataFrame(np.arange(10, 22).reshape(3, 4),
                index=['r1', 'r2', 'r3'],
                columns=['A', 'B', 'C', 'D'])
print(df); print('-----------------------------------')
print(df.loc[df.A>10, 'B']); print('-----------------------------------')
print(df.loc[df.A>10, ['B', 'C']]); print('-----------------------------------')