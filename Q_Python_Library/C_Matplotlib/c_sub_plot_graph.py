import matplotlib.pyplot as plt
import numpy as np

# plot first
x = np.array([0,1,2,3])
y = np.array([4,5,6,7])

plt.subplot(1,2,1)  # (row, col, index)
plt.plot(x, y)

# plot second

x = np.array([0,1,2,3,4])
y = x + 10

plt.subplot(1,2,2)
plt.plot(x, y, marker = 'o')
plt.show()