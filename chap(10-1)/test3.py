import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv(
    'https://raw.githubusercontent.com/dongupak/DataSciPy/master/data/csv/weather.csv',
    encoding='cp949'
)

weather.fillna(0, inplace=True)
print(weather[weather['평균풍속'] == 0.0])