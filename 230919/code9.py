# 연습5

import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt

np.random.seed(20230919)

N_CLASSES, N_SAMPLES = 4, 100
STD = 0.3
MEANS = [[1, 1], [-1, -1], [-1, 1], [1, -1]]

X, y = [], []
for class_idx in range(N_CLASSES):
    mean = MEANS[class_idx]
    X_class = normal(loc=mean, scale=STD,
                     size=(N_SAMPLES, 2))
    y_class = class_idx * np.ones(N_SAMPLES)

    X.append(X_class); y.append(y_class)
X, y = np.vstack(X), np.concatenate(y)

fig, ax = plt.subplots(figsize=(10, 10))
for class_idx in range(N_CLASSES):
    X_class = X[y == class_idx]
    ax.scatter(X_class[:, 0], X_class[:, 1],
               label=f"class {class_idx}")

ax.legend(fontsize=15)
ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')

ax.tick_params(labelsize=15)
plt.show()