import pandas as pd

s=pd.Series([9904312, 3448737, 2890451, 246052],
            index=['서울', '부산', '인천', '대구'])

print(s[3], s['대구'])
print(s[[0, 3]], '\n', s[['서울', '대구']])
print(s[(250e4<s)&(s<500e4)])