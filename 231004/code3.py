import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs

from utils import vis_geometric_dataset

X, y, centers = make_blobs(return_centers=True)
print(f'X shape: {X.shape}')
print(y)