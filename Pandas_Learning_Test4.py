import numpy as np
import pandas as pd

dates = pd.date_range('20191201', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[2, 3] = np.nan
print(df)
# 空值处理

# 首先判断是不是缺失数据呢
print(df.isnull())
print(np.any(df.isnull()) == True) #True就是有空值

#print(df.dropna(axis=0, how='any'))  # how = {'any','all'} 全部等于nan才是all

# 默认为一个别的数据
#print(df.fillna(value=-999))
