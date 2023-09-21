# 연습

import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt

np.random.seed(0)

N_CLASSES, N_SAMPLES = 10, 100
STD = 0.3
MEANS = np.random.uniform(-5, 5, (N_CLASSES, 2))

X, y = [], []
for class_idx in range(N_CLASSES):
    mean = MEANS[class_idx]
    X_class = normal(loc=mean, scale=STD, size=(N_SAMPLES, 2))
    y_class = class_idx * np.ones(N_SAMPLES)

    X.append(X_class), y.append(y_class)
X, y = np.vstack(X), np.concatenate(y)

### 시각화
fig, ax = plt.subplots(figsize=(10, 10))
for class_idx in range(N_CLASSES):
    X_class = X[y == class_idx]
    ax.scatter(X_class[:, 0], X_class[:, 1],
               label=f"class {class_idx}",
               alpha=0.5)

ax.legend(fontsize=15)
ax.axhline(y=0, c='gray');ax.axvline(x=0, c='gray')
ax.tick_params(labelsize=15)
plt.show()