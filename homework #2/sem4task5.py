import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('BTC_data.csv')

fig = plt.figure(figsize = (100,20))
ax1 = fig.add_subplot(111)

x = df['time']
y = df['close']


ax1.plot(x, y,'r')
ax1.scatter(x, y, marker='x')
ax1.set_title('BTC$$$')

ax1.grid()

plt.show()