# dataset_utils 함수 쓰기

import numpy as np
import matplotlib.pyplot as plt

from dataset_utils import make_dataset, vis_dataset

np.random.seed(0)

n_classes = 10

X, y = make_dataset(n_classes=n_classes)
print(y) # y값 shuffing된 거 확인
fig, ax = vis_dataset(X, y)
plt.show()