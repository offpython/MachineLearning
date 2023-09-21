# shuffling

import numpy as np
from dataset_utils import make_dataset, vis_dataset

# 1차원 데이터의 Shuffling
A = np.arange(10)
print(A)

np.random.shuffle(A)
print(A)

# 2차원 데이터의 Shuffling
## 2차원 행렬을 shuffling 해주면, row가 shuffling 됨
A = np.arange(12).reshape(3, 4)
print(A, '\n')
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]] 
'''

np.random.shuffle(A)
print(A)
'''
[[ 4  5  6  7] --- (2)
 [ 0  1  2  3] --- (1)
 [ 8  9 10 11]] --- (3)
'''

# Data Shuffling할 때의 주의점 -> 문제점: X, y의 pair 관계가 없어짐
X, y = make_dataset(n_classes=n_classes)
np.random.shuffle(X)
np.random.shuffle(y)

