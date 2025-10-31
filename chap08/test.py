import pandas as pd

s1=pd.Series([9904312, 3448737, 2890451, 2466052],
             index=['서울', '부산', '인천', '대구'],
             name='인구수')

s1.name = '인구'
s1.index.name = '도시'

print(s1, '\n')
print('대구 인구= ', s1['대구'])

s2=pd.Series(range(10, 14))
print(s2)

s2=pd.Series(["Hello", "World", 1, 2])
print(s2)
print(s2[0])