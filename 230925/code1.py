import matplotlib.pyplot as plt

from dataset_utils import make_dataset

X = make_dataset(std=0.3)

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(X[:, 0], X[:, 1])

ax.tick_params(labelsize=15)
plt.show()