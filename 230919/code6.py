# 연습2
import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt

np.random.seed(20230919)

n_samples = 100
std = 0.3
x1 = normal(loc=[1, 1], scale=std, size=(n_samples, 2))
x2 = normal(loc=[1, -1], scale=std, size=(n_samples, 2))
x3  = normal(loc=[-1, -1], scale=std, size=(n_samples, 2))

dataset = np.vstack([x1, x2, x3])

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(dataset[:, 0], dataset[:, 1])

ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')

ax.tick_params(labelsize=15)
plt.show()