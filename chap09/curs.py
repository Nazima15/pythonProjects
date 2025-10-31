# import pandas as pd 
# python_df = pd.read_excel('특강신청명단.xlsx', sheet_name='파이썬특강') 
# students_df = pd.read_excel('특강신청명단.xlsx', sheet_name='학생목록') 
# merged_df = python_df.merge(students_df, how='left', on='학번') 
# merged_df.drop(columns=['이름_y'],inplace=True) 
# merged_df.rename(columns={'이름_x':'이름'}, inplace=True) 
# print(merged_df) 
# merged_df.to_excel('파이썬.xlsx') 

import pandas as pd 
import numpy as np 
java_df = pd.read_excel('특강신청명단.xlsx', sheet_name='자바특강') 
python_df = pd.read_excel('특강신청명단.xlsx', sheet_name='파이썬특강') 
students_df = pd.read_excel('특강신청명단.xlsx', sheet_name='학생목록') 
merged_df = students_df.merge(java_df, how='left', indicator=True) 
merged_df['자바특강'] = '' 
merged_df.loc[merged_df['_merge'] == 'both', '자바특강'] = '신청' 
merged_df = merged_df.drop(columns=['_merge']) 
merged_df = merged_df.merge(python_df, how='left', indicator=True) 
merged_df['파이썬특강'] = '' 
merged_df.loc[merged_df['_merge'] == 'both', '파이썬특강'] = '신청' 
merged_df = merged_df.drop(columns=['_merge']) 
print(merged_df) 
merged_df.to_excel('모든과목.xlsx', index=False) 


