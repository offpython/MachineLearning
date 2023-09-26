import numpy as np
import matplotlib.pyplot as plt

from dataset_utils import make_dataset, vis_dataset
from dataset_utils import get_db_X

K = 5
N_CLASSES = 4
X, y = make_dataset(n_classes=N_CLASSES)

fig, ax = vis_dataset(X, y)

db_X = get_db_X(ax)

db_y = []
for X_ in db_X:
    dists = np.sum((X - X_) ** 2, axis=1)

    sorted_indices = np.argsort(dists)
    closest_indices = sorted_indices[:K]
    closest_classes = y[closest_indices]

    uniques, cnts = np.unique(closest_classes,
                              return_counts=True)
    pred = uniques[np.argmax(cnts)]
    db_y.append(pred)
db_y = np.array(db_y)

for class_idx in range(N_CLASSES):
    class_X = db_X[db_y == class_idx]
    ax.scatter(class_X[:, 0], class_X[:, 1],
               color=f"C{class_idx}", alpha=0.1)

plt.show()