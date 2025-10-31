import pandas as pd 
orders_df = pd.read_excel('data.xlsx') 
orders_df['판매금액'] = orders_df['가격'] * orders_df['판매수량'] 
# 카테고리별 총 판매액 
category_sales = orders_df.groupby('카테고리')['판매금액'].sum().reset_index() 
print(category_sales) 
#카테고리별 총 판매 수량 
category_stats = orders_df.groupby('카테고리').agg(총판매수량=('판매수량', 'sum')).reset_index() 
print(category_stats)
