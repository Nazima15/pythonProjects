import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

# 인코딩 수정: CD949 → cp949
weather = pd.read_csv(
    'https://raw.githubusercontent.com/dongupak/DataSciPy/master/data/csv/weather.csv',
    encoding='cp949'
)

weather.dropna(axis=0, how='any', inplace=True)
print(weather[weather['평균풍속'].isna() == True])
