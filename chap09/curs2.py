import pandas as pd
input_df = pd.read_excel('입력파일.xlsx', dtype=str)
input_df = input_df.drop(columns=['id', 'email', 'address', 'major', 'status'])
input_df = input_df.rename(columns={'studentNumber':'학번', 'studentName':'이름', 'contact':'연락처'});
input_df.to_excel('출력파일.xlsx', index=False)