import matplotlib.pyplot as plt

from sklearn.datasets import make_circles

from utils import vis_geometric_dataset

X, y = make_circles(n_samples=[100, 300],
                    noise=0.05, factor=0.4)
fig, ax = vis_geometric_dataset(X, y)
plt.show()