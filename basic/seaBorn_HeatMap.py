import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

csv_data_df = pd.read_csv('C:/Users/tzin/Documents/Python/HeatMap/malibu_shmoo_rt_2nd_chip9.csv')
#ori_file = open("C:\\Users\\tzin\\Documents\\Python\\eflash_1MHz_sweep\\eflash_chipNo_121_SLC.txt", 'r', encoding='utf-8-sig')

print(csv_data_df.head())

df = csv_data_df.pivot('VDD [V]', 'Frequency [MHz]', 'pass/fail')
print(df.head())


plt.rcParams['figure.figsize'] = [10, 8]

plt.pcolor(df)

plt.xticks(np.arange(0.5, len(df.columns),1), df.columns, fontsize = 18)
plt.yticks(np.arange(0.5, len(df.index), 1), df.index, fontsize = 18)
plt.tick_params(axis='x', length=5, pad=7, labelsize=15, which='major')
plt.tick_params(axis='y', length=5, pad=7, labelsize=15)
plt.xlabel('Volt', fontsize=20, labelpad=8)
plt.ylabel('Freq', fontsize=20, labelpad=8)
# plt.colorbar()

# new_order = ['24', '22', '20', '18', '16']
# df = df.reindex(new_order)

#annotate each cell with the numeric value of integer format
# sns.heatmap(df, annot=True, fmt='d', cmap='RdYlGn_r')
sns.set_theme(style="whitegrid", font="Times New Roman")
ax = sns.heatmap(df, annot=False,annot_kws={"size":17}, square = True ,fmt='d', cmap='RdYlGn_r', vmax=1, vmin=0, linewidths=0.1, linecolor='white', cbar=False)
ax.invert_yaxis()
plt.title('Malibu shmoo plot VRD 0.8V @RT, chip9', fontsize=20, pad=20)
plt.show()




'''
# matplot lib을 이용한 히트맵 그리기 (Heatmap by mat Plot Library)
plt.pcolor(df)
plt.xticks(np.arange(0.5, len(df.columns),1), df.columns)
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.title('Heatmap by plt.pcolor()', fontsize=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Month', fontsize=14)
plt.colorbar()

plt.show()


#heatmap by SeaBorn

ax = sns.heatmap(df)
plt.title('Heatmap of Flight by seaborn', fontsize=20)
# plt.show()


#annotate each cell with the numeric value of integer format
sns.heatmap(df, annot=True, fmt='d')
plt.title('Annotated cell with numeric value', fontsize=20)
# plt.show()

# different colormap
sns.heatmap(df, cmap='RdYlGn_r')
plt.title('colormap of cmap=RdYlGn_r', fontsize=20)
# plt.show()

# different colormap
sns.heatmap(df, cmap='YlGnBu')
plt.title('colormap of cmap=YlGnBu', fontsize=20)
# plt.show()

#  center the colormap at a specific value
sns.heatmap(df, center = df.loc['Jan', 1949])
plt.title('Center the colormap at Jan. 1949', fontsize=20)
# plt.show()


# heatMap by PANDAS
df.style.background_gradient(cmap='summer')
plt.pcolor(df)

plt.show()

'''