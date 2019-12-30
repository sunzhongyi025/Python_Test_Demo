import pandas as pd
import numpy as np

# 选择数据
dates = pd.date_range('20191201', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['a', 'b', 'c', 'd'])
# print(df)


# 选择某一列
# print(df['c'])

# 切片选择
# print(df[2:4])
# print(df['20191203':'20191204'])#按照索引

# 按标签选择
# print(df.loc['20191204'])
# print(df.loc['20191205', ['d', 'a']])

# 按位置选
# print(df.iloc[2:4,1:5])
# print(df.iloc[[1,4],1:3])

# 综合筛选
# print(df.ix[2:4, ['a', 'd']])


# 布尔检索
# A这一列中大于8的
print(df[df.a > 8])
