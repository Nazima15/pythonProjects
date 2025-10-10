import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv('babies.csv')

plt.bar(data.Year, data.Babies)
plt.title("Numbers per year")       # 그래프 제목
plt.xlabel("Year")             # Y축 이름
plt.ylabel("Number of Births")  # X축 이름'

plt.savefig("numbers_per_year.png", dpi=600)
plt.show()