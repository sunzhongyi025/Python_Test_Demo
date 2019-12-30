# Merge 合并方式

import numpy as np
import pandas as pd

# 基于Key合并到一起
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
res = pd.merge(left, right, on='key')
#

# 如果有两个key的时候
left = pd.DataFrame({'key': ['K0', 'K0', 'K2', 'K3'],
                     'key01': ['K2', 'K2', 'K0', 'K2'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K2', 'K2', 'K1'],
                      'key01': ['K2', 'K2', 'K2', 'K2'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
res = pd.merge(left, right, on=['key', 'key01'], how='inner')  # 只把两个key都一样的才合并
# how = {'left','right','outer','inner'}


# indicater 属性
df1 = pd.DataFrame({'cols1': [0, 1], 'col_left': ['a', 'b']})
df2 = pd.DataFrame({'cols1': [1, 2, 2], 'col_left': [2, 2, 2]})
res = pd.merge(df1, df2, on='cols1', how='outer', indicator='Indicator_Column')

# index 属性
left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']},
                    index=['K1', 'K2', 'K3', 'K4'])
right = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']},
                     index=['K0', 'K1', 'K2', 'K3'])

res = pd.merge(left, right, left_index=True, right_index=True, how='inner')

# 处理重复名字的属性，但是意义不同
boys = pd.DataFrame({'k': ['K1', 'K2', 'K3'], 'age': [16, 19, 20]})
grils = pd.DataFrame({'k': ['K1', 'K1', 'K4'], 'age': [20, 25, 27]})
res = pd.merge(boys, grils, on='k', suffixes=['_boys', '_grils'], how='outer')
print(res)
