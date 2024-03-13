import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(150, 20, size=100)
print(x)
plt.hist(x)
plt.show()
