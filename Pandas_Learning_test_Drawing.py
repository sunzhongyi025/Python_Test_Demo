import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# plot data
# series
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()
#data.plot()
#plt.show()

# Dataframe
data=pd.DataFrame(np.random.randn(1000,4),
                  index=np.arange(1000),
                  columns=list('ABCD'))
data=data.cumsum()
print(data.head(3))
AX=data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class 1')
BX=data.plot.scatter(x='A',y='C',color='Orange',label='Class 2',ax=AX)
plt.show()