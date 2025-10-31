import pandas as pd

# CSV 파일 읽기 (인덱스 첫 번째 컬럼 사용)
df = pd.read_csv('weather_utf.csv', encoding='utf-8', index_col=0)

# 컬럼 이름 공백 제거 및 °C 제거 등 정리
df.columns = df.columns.str.replace(' ', '').str.replace('°C', '').str.replace('(', '').str.replace(')', '')

# 컬럼 이름 확인
print("컬럼 이름:", df.columns)
print('-------------------')

# 각 컬럼의 데이터 개수 확인
print(df.count())
print('-------------------')

# 전체 컬럼 평균
print(df.mean())
print('-------------------')

# 평균기온 컬럼 평균
print(df['평균기온'].mean())
print('-------------------')

# 평균기온이 4 이상인 값만 평균
print(df.loc[df['평균기온'] >= 4, '평균기온'].mean())
