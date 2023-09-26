# 연습 -> 실제 데이터에서 centroid 뽑음

import numpy as np
import matplotlib.pyplot as plt
from dataset_utils import make_dataset

K = 4
X = make_dataset(std=0.4)
n_samples = X.shape[0]

random_indices = np.arange(400) # 0~399
np.random.shuffle(random_indices) # random하게 섞기
random_indices = random_indices[:K] # K개 인덱스 뽑기
centroids = X[random_indices] # 실제 존재하는 데이터에서 K개를 centroid로 가정
X_ = X.reshape(n_samples, 1, 2)  # (400, 1, 2)
centroids_ = centroids.reshape(1, K, 2) # (1, 4, 2)

dists = np.sum((X_ - centroids_)**2, axis=2)  # (400 -> samples, 4 -> cluster)
clustering_indices = np.argmin(dists, axis=1) # 가까운 cluster 인덱스
# 어떤 centroids와 가장 가까운지 400개 마다 구한 결과임

