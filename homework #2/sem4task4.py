import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('iris_data.csv')

fig = plt.figure(figsize=(16, 25))
ax1 = fig.add_subplot(611)
ax2 = fig.add_subplot(612)
ax3 = fig.add_subplot(613)
ax4 = fig.add_subplot(614)
ax5 = fig.add_subplot(615)
ax6 = fig.add_subplot(616)

x = df['SepalLengthCm']
y = df['SepalWidthCm']
k = df['PetalLengthCm']
l = df['PetalWidthCm']

ax1.plot(x, y, 'b.')
ax2.plot(x, k, 'b.')
ax3.plot(x, l, 'b.')
ax4.plot(y, k, 'b.')
ax5.plot(y, l, 'b.')
ax6.plot(k, l, 'b.')
ax1.set_title('1 graph')
ax2.set_title('2 graph')
ax3.set_title('3 graph')
ax4.set_title('4 graph')
ax5.set_title('5 graph')
ax6.set_title('6 graph')

ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
ax5.grid()
ax6.grid()

plt.show()