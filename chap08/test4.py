import pandas as pd

s=pd.Series([9904312, 3448737, 2890451, 2466052],
            index=['서울', '부산', '인천', '대구'])

print(s[1:3])
print(s["부산":"대구"])