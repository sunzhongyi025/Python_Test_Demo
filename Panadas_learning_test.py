import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1])
# print(s)

dates = pd.date_range('20190101', '20190106', periods=6)
# print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
# print(df)

df1 = pd.DataFrame({'a': 1.,
                    'B': pd.Timestamp('20191230'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'd': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(['sun', 'wu', 'sun', 'wu']),
                    'f': 'LOVE'},
                   index=['S', 'u', 'n', 'z'])
# print(df1)
df1.sort_index(axis=1, ascending=False)
print(df1.sort_values(by='E', ascending=False))
print(df1)
print(df1.dtypes)
print(df1.index)
print(df1.columns)
print(df1.values)

print(df1.describe())
