import pandas as pd
import numpy as np

dates = pd.date_range('20191201', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)

df.iloc[2, 2] = 1111  # 第二列第二行改为1111
print(df)

df.loc['20191201', 'B'] = 2222
print(df)

# df[df['A']>2]=0
# print(df)


# 将与A列大于10所对应的B列的值改为0的两种方式
df['B'][df['A'] > 10] = 0
df.B[df.A > 10] = 0
print(df)

# 增加新的一行
df['F'] = np.nan
print(df)

df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20191201', periods=6))
print(df)
