import pandas as pd
data={'key1':['a', 'b', 'c', 'd', 'e'],
      'key2':['v', 'w', 'x', 'y', 'z'],
      'col':[1, 2, 3, 4, 5],}

df=pd.DataFrame(data, columns=['key1', 'key2', 'col'])

print(df.duplicated(['key1']))
print('-----------------------')
print(df.duplicated(['key1', 'key2']))