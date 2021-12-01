import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\jinnoo\Desktop\오픈소스개발\시군구별_용도지역별_이용상황별_지가변동률_20211126163556.csv',
                 encoding = 'cp949')

plt.hist(df['주거지역'], alpha=0.4, bins=7, rwidth=1, color='blue')
plt.show()
print(df.groupby('지역별(1)')['주거지역'].mean())

