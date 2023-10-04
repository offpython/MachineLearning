import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs

from utils import vis_geometric_dataset

X, y = make_blobs()
print("===== X =====")
print(f"type: {type(X)}")
print(f"shape: {X.shape}")

print("===== y =====")
print(f"type: {type(y)}")
print(f"shape: {y.shape}")
print(f"values: {y}")
uniques, cnts = np.unique(y, return_counts=True)
print(f"unique / cnts: {uniques} / {cnts}")

fig, ax = vis_geometric_dataset(X, y)
plt.show()