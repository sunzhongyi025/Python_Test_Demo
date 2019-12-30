import pandas as pd
import numpy as np

# concatenating
df1 = pd.DataFrame(np.zeros((3, 4)), columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)), columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(2 * np.ones((3, 4)), columns=['a', 'b', 'c', 'd'])

# 合并纵向
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res)

# 扩展,有一些重复属性，有一些不重复
df4 = pd.DataFrame(np.zeros((3, 4)), columns=['a', 'b', 'c', 'd'], index=[0, 1, 2])
df5 = pd.DataFrame(np.ones((3, 4)), columns=['e', 'b', 'g', 'd'], index=[1, 2, 3])
res = pd.concat([df4, df5], join='inner', ignore_index=True)  # join = {'outer','inner'},后者只选择重合部分
print(res)

# 横向左右合并的时候
res = pd.concat([df4, df5], axis=1, join_axes=[df5.index])
print(res)

# append 类似于arcgis一样的
s1 = pd.Series([5, 6, 7, 1], index=['a', 'b', 'c', 'd'])
res = df1.append(s1, ignore_index=True)
print(res)
