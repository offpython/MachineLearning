# Dataset 만들어주는 함수 만들기

import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt
np.random.seed(0)

def make_dataset(n_classes=4, n_class_samples=100,
                 std=0.5, means=None):
    if means == None:
        means = np.random.uniform(-5, 5, (n_classes, 2))

    X, y = [], []
    for class_idx in range(n_classes):
        mean = means[class_idx]

        X_class = normal(loc=mean, scale=std,
                         size=(n_class_samples, 2))
        y_class = class_idx * np.ones(n_class_samples)

        X.append(X_class)
        y.append(y_class)

    X, y = np.vstack(X), np.concatenate(y)
    return X, y

n_classes = 10
X, y = make_dataset(n_classes=n_classes)

fig, ax = plt.subplots(figsize=(10, 10))
for class_idx in range(n_classes):
    X_class = X[y == class_idx]
    ax.scatter(X_class[:, 0], X_class[:, 1],
               label=f"class {class_idx}",
               alpha=0.5)

ax.legend(fontsize=15)
ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')

ax.tick_params(labelsize=15)
plt.show()
