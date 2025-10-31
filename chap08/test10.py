import pandas as pd


df = pd.read_excel('data.xlsx')
df['사은품']=df['결제금액']>20000
print(df)

df['사은품']=df['사은품'].map({True:'지급', False:'미지급'})
print(df)

df.to_excel('result.xlsx', index=False)
