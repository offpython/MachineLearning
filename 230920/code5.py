import numpy as np
import matplotlib.pyplot as plt
from dataset_utils import make_dataset, vis_dataset

np.random.seed(0)

### Dataset 준비 ###
n_classes = 3
X, y = make_dataset(n_classes=n_classes)

### 분류 준비 ###
K = 5
test_data = np.array([2, 1.2])

### 분류하기 ###
dists = []
for X_ in X:
    dist = np.sqrt(np.sum((test_data - X_)**2))
    dists.append(dist)

sorted_indices = np.argsort(dists)      # argsort => 인덱스
closest_indices = sorted_indices[:K]    # 가까운 k개 데이터의 인덱스
closest_classes = y[closest_indices]    # 가가운 데이터들의 클래스

uniques, cnts = np.unique(closest_classes, return_counts=True)
pred = uniques[np.argmax(cnts)]
print(f"{test_data} is classified as {pred}\n")


### 결과 시각화하기 ###
closest_X = X[closest_indices]

fig, ax = vis_dataset(X, y)
ax.scatter(test_data[0], test_data[1], color='red', s=300,
           edgecolor=f'C{int(pred)}', linewidths=5)         # 테두리 값 바꿔줌

for closest_X_, closest_class in zip(closest_X, closest_classes):
    ax.plot([closest_X_[0], test_data[0]], # x 좌표들
            [closest_X_[1], test_data[1]], # y 좌표들
            color=f'C{int(closest_class)}', # 색깔은 class를 보고 결정
            ls=':') # 점선으로 그리기
plt.show()