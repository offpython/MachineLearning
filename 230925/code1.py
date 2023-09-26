# K-means Clustering 구현하기

import numpy as np
import matplotlib.pyplot as plt
from dataset_utils import make_dataset

# step.1 데이터셋과 초기 Centroid
K = 4
X = make_dataset(std=0.4)
n_samples = X.shape[0]

random_indices = np.arange(400) # 0~399
np.random.shuffle(random_indices) # random하게 섞기
random_indices = random_indices[:K] # K개 인덱스 뽑기
centroids = X[random_indices] # 실제 존재하는 데이터에서 K개를 centroid로 가정

# step.2 데이터마다 Centroid와의 거리를 구하고, 가장 가까운 centroid 인덱스 구하기
X_ = X.reshape(n_samples, 1, 2) # (400, 1, 2)
for step in range(5):
    centroids_ = centroids.reshape(1, K, 2) # (1, 4, 2)

    dists = np.sum((X_ - centroids_) ** 2, axis=2) # (400 -> sample, 4 -> cluster)
    clustering_indices = np.argmin(dists, axis=1) # 가까운 cluster의 인덱스

# Step.3 같은 Cluster의 데이터 모으기
clustering_dict = {}
for k in range(K):
    cluster_X = X[clustering_indices == k]
    clustering_dict[k] = cluster_X

# 시각화
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].scatter(X[:, 0], X[:, 1], alpha=0.5)
for k in range(K):
    cluster_X = clustering_dict[k]
    axes[1].scatter(cluster_X[:, 0], cluster_X[:, 1], alpha=0.5)
plt.show()

# Step.4 Centroid Update
centroids = []
for k in range(K):
    centroid = np.mean(clustering_dict[k], axis=0)
    centroids.append(centroid)
centroids = np.concatenate(centroids).reshape(K, 2)

# Step.5 반복 적용하기
for step in range(5): # 총 5번 update
    centroids_ = centroids.reshape(1, K, 2)

    dists = np.sum((X_ - centroids_) ** 2, axis=2)
    clustering_indices = np.argmin(dists, axis=1)

    clustering_dict = {}
    for k in range(K):
        cluster_X = X[clustering_indices == k]
        clustering_dict[k] = cluster_X

    centroids = []
    for k in range(K):
        centroid = np.mean(clustering_dict[k], axis=0)
        centroids.append(centroid)
    centroids = np.concatenate(centroids).reshape(K, 2)

# Step.6 시각화 추가하기
fig, axes = plt.subplots(2, 3, figsize=(15, 10)) ###
axes = axes.flatten() ###
axes[0].scatter(X[:, 0], X[:, 1]) ###
for step in range(5):
    centroids_ = centroids.reshape(1, K, 2)

    dists = np.sum((X_ - centroids_) ** 2, axis=2)
    clustering_indices = np.argmin(dists, axis=1)

    clustering_dict = {}
    for k in range(K):
        cluster_X = X[clustering_indices == k]
        clustering_dict[k] = cluster_X

        axes[step + 1].scatter(cluster_X[:, 0], cluster_X[:, 1]) ###

    centroids = []
    for k in range(K):
        centroid = np.mean(clustering_dict[k], axis=0)
        centroids.append(centroid)
    centroids = np.concatenate(centroids).reshape(K, 2)

plt.show()

