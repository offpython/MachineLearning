import numpy as np
from sklearn.datasets import make_blobs

dataset = make_blobs()
# print(type(dataset)) # <class 'tuple'>
# print(len(dataset)) # 갯수 2개

X, y = make_blobs()
print('===== X =====')
print(type(X)) # <class 'numpy.ndarray'>
print(X.shape) # (100, 2)
print(y.shape) # (100,)
print(y)

print(np.unique(y, return_counts=True)) # (array([0, 1, 2]), array([34, 33, 33]))
