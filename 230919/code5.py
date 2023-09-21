# 연습1

import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt

N_SAMPLES = 100
x = normal(loc=0, scale=3, size=(N_SAMPLES,))
y = normal(loc=-2, scale=1, size=(N_SAMPLES,))
dataset = np.hstack([x.reshape(N_SAMPLES, 1),
                     y.reshape(N_SAMPLES, 1)])

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(dataset[:, 0], dataset[:, 1])

ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')

ax.tick_params(labelsize=15)
plt.show()