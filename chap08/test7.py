import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(10, 22).reshape(3, 4),
                  index=["r1", "r2", "r3"],
                  columns=["A", "B", "C", "D"])

print(df)
print('-----------------------------------')

# 라벨 기반 인덱싱
print(df.loc["r2"])
print('-----------------------------------')

# 위치 기반 인덱싱
print(df.iloc[1:3])
