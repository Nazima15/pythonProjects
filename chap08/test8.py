import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(10, 22).reshape(3, 4),
                  index=['r1', 'r2', 'r3'],
                  columns=['A', 'B', 'C', 'D'])

# 1. 전체 데이터
print(df.loc[:, :])
print('-----------------------------------')

# 2. r2~r3 행의 B열
print(df.loc['r2':'r3', 'B'])
print('-----------------------------------')

# 3. r2행의 B~C열
print(df.loc['r2', 'B':'C'])
print('-----------------------------------')

# 4. iloc를 이용한 위치 기반 접근 (정수 인덱스)
# r2 = 1번째 행, B:C = 1~2번째 열
print(df.iloc[1, 1:3])
print('-----------------------------------')

# 5. iloc로 단일 값
print(df.iloc[1, 1])
print('-----------------------------------')
