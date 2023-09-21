# 해결법
'''
1) 0~n까지의 index를 먼저 만들고, 이 index를 섞어준다.
2) 랜덤하게 섞인 index로 X, y를 인덱싱해준다. 그러면 pair는 깨지지 않는다.
--------
indices = np.arange(len(y))
np.random.shuffle(indices)
X, y = X[indices], y[indices]
'''

import numpy as np
from numpy.random import normal
from numpy.random import uniform
import matplotlib.pyplot as plt
from dataset_utils import make_dataset, vis_dataset

def make_dataset(n_classes=4, n_class_samples=100,
                 std=0.5, means=None, shuffle=True):
    if means == None:
        means = uniform(-5, 5, (n_classes, 2))

    X, y = [], []
    for class_idx in range(n_classes):
        mean = means[class_idx]

        X_class = normal(loc=mean, scale=std,
                         size=(n_class_samples, 2))
        y_class = class_idx * np.ones(n_class_samples)

        X.append(X_class)
        y.append(y_class)

    X, y = np.vstack(X), np.concatenate(y)

    if shuffle:
        indices = np.arange(len(y))
        np.random.shuffle(indices)

        X, y = X[indices], y[indices]
    return X, y
