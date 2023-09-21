# Random Dataset 만들기 연습

import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt

np.random.seed(0)

n_sample = 100
x = np.random.normal(loc=0, scale=3, size=(n_sample,))
y = np.random.normal(loc=-2, scale=1, size=(n_sample,))

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(x, y)

ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')

ax.tick_params(labelsize=15)
plt.show()
