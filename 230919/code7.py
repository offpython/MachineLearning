# 연습3

import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt

np.random.seed(20230919)

N_SAMPLES = 100
STD = 0.3
X1 = normal(loc=[1, 1], scale=STD, size=(N_SAMPLES, 2))
X2 = normal(loc=[-1, -1], scale=STD, size=(N_SAMPLES, 2))

y1 = 0 * np.ones(N_SAMPLES)
y2 = 1 * np.ones(N_SAMPLES)

X = np.vstack([X1, X2]) # (100, 2) + (100, 2) = (200, 2)
y = np.concatenate([y1, y2]) # (100,) + (100,) = (200,)

fig, ax = plt.subplots(figsize=(10, 10))
X_ones, X_zeros = X[y == 1], X[y == 0]
ax.scatter(X_ones[:, 0], X_ones[:, 1], color='blue')
ax.scatter(X_zeros[:, 0], X_zeros[:, 1], color='red')

ax.axhline(y=0, color='gray'); ax.axvline(x=0, color='gray')
ax.tick_params(labelsize=15); plt.show()
