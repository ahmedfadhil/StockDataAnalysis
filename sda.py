import datetime as dt
import pandas as pd
import numpy as np
from matplotlib import style
import pandas_datareader as web
import matplotlib.pyplot as plt
from matplotlib import *

style.use('ggplot')

df = pd.read_csv('data.csv', parse_dates=True, index_col=0)
df['100ma'] = df['Close'].rolling(window=100, min_periods=0).mean()
df.dropna(inplace=True)
print(df.head())
# print(df.tail())


ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])
plt.show()
