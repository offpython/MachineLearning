# Inter-cluster Distance를 측정해서 학습하는 전체 코드

import numpy as np
import matplotlib.pyplot as plt

from dataset_utils import make_dataset
from utils import cal_inter_cluster_dist

K = 4
X = make_dataset(std=0.4)
n_samples = X.shape[0]

random_indices = np.arange(400)
np.random.shuffle(random_indices)
random_indices = random_indices[:K]
centroids = X[random_indices]

inter_cluster_dists = [cal_inter_cluster_dist(centroids)]
X_ = X.reshape(n_samples, 1, 2)

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

    inter_cluster_dists.append(cal_inter_cluster_dist(centroids))

plt.show()
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(inter_cluster_dists)
plt.show()