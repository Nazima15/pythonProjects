import matplotlib.pyplot as plt
import numpy as np

years = [1965, 1975, 1985, 1995, 2005, 2015]
ko = [130, 650, 2450, 11600, 17790, 27250]
jp = [890, 5120, 11500, 42130, 40560, 38780]
ch = [100, 200, 290, 540, 1760, 7940]

x = np.arange(len(years))   # x축 위치
width = 0.25                # 막대 너비

plt.bar(x - width, ko, width, label='Korea')
plt.bar(x, jp, width, label='Japan')
plt.bar(x + width, ch, width, label='China')

plt.xticks(x, years)
plt.ylabel("GDP per capita")
plt.legend()
plt.show()
