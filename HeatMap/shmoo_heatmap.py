import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.colors as mcl
import matplotlib.cm as cmap
import seaborn as sns

from matplotlib.colors import LinearSegmentedColormap

h = 24
s = 0.99
v = 1

colors = [
    mcl.hsv_to_rgb((h/360, 0, v)), 
    mcl.hsv_to_rgb((h/360, 0.5, v)),
    mcl.hsv_to_rgb((h/360, 1, v))
]

cmap = LinearSegmentedColormap.from_list('my_cmap',colors,gamma=3)

csv_data_df = pd.read_csv('malibu_shmoo.csv')

print(csv_data_df)

df = csv_data_df.pivot('Frequency [MHz]', 'VDD [V]', 'result')

print(df)

cmap = plt.get_cmap('YlGn_r') # apply ColorMap 잘못된 것 넣으면 내가 넣을 수 cmap들을 알려준다
plt.set_cmap(cmap)

plt.rcParams['figure.figsize'] = [10, 8]
# plt.pcolor(df)
# plt.xticks(np.arange(0.5, len(df.columns),1), df.columns)
# plt.yticks(np.arange(0.5, len(df.index), 1), df.index)

# plt.title('Shmoo ', fontsize=18)
plt.xlabel('VDD [V]', fontsize=18)
plt.ylabel('Frequency[MHz]', fontsize=18)
# plt.grid(color='#BDBDBD', linestyle='-', linewidth=2,)
# # plt.colorbar()
# plt.show()

sns.heatmap(df, annot=True, fmt='d', cmap='YlGn_r', square = True ,linecolor='gray', linewidths=0.5, cbar=False, ) ## annot 숫자 표기, cmap='RdYlGn_r' 에서 _r은 reverse이다. 빨강이 하한값으로할지, 녹색을 하한값으로 할지임, square=는 정사각형, cbar 는 칼라막대 여부, cmap 적용
# sns.heatmap(df, annot=True, fmt='d', square = True ,linecolor='gray', linewidths=0.5, cbar=False, ) ## annot 숫자 표기, cmap='RdYlGn_r' 에서 _r은 reverse이다. 빨강이 하한값으로할지, 녹색을 하한값으로 할지임, square=는 정사각형, cbar 는 칼라막대 여부
plt.title('shmoo', fontsize=25)
plt.show()



'''
# print(df.head())
asdf_list = []
for i in range(0, len(csv_data_df.columns)-1):
    # asdf_list.append(csv_data_df.loc[i:i,['freq','0.80 V']])
    volt = 0.80 + i*0.05
    columnName = "%.2f V" % volt
    asdf_list.append(csv_data_df[["freq", columnName]].values.tolist())
    for j in range(0, len(asdf_list[i])):
        asdf_list[i][j].extend([columnName])

print(asdf_list)

df = pd.DataFrame(asdf_list)

print(df)
'''