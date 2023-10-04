import matplotlib.pyplot as plt

from sklearn.datasets import make_moons

from utils import vis_geometric_dataset

X, y = make_moons(n_samples=[100, 300],
                  noise=0.05)
fig, ax = vis_geometric_dataset(X, y)
plt.show()
