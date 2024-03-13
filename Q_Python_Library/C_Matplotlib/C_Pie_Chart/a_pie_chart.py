import matplotlib.pyplot as plt
import numpy as np

y = np.array([45, 70, 80, 92])  # Valores de la variable dependiente (Y)
mylabels = ["apple", "banana", "Cherries", "Dates"]
plt.pie(y, labels=mylabels, startangle=45)
plt.show()
