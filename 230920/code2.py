# Dataset, Test data, 준비하기

import numpy as np
import matplotlib.pyplot as plt
from dataset_utils import make_dataset, vis_dataset

np.random.seed(0)

n_classes = 3
X, y = make_dataset(n_classes=n_classes)
print(X.shape)
test_data = np.array([-2, -0.5])

# Test_data와 dataset 안에 있는 모든 데이터 사이의 거리
K = 5
dists = []
for X_ in X:
    dist = np.sqrt(np.sum((test_data - X_)**2))
    dists.append(dist)

sorted_indices = np.argsort(dists)
closest_indices = sorted_indices[:K] # 가까운 K개 데이터의 인덱스
closest_classes = y[closest_indices] # 가까운 데이터들의 클래스

print(sorted_indices)
print(closest_classes)


# fig, ax = vis_dataset(X, y)
# ax.scatter(test_data[0], test_data[1], color='red', s=100)
# plt.show()

