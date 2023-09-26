import numpy as np


def cal_inter_cluster_dist(centroids):
    K = centroids.shape[0]

    centroids_v = centroids.reshape(K, 1, 2)
    centroids_h = centroids.reshape(1, K, 2)

    cen_dists = np.sum((centroids_v - centroids_h)**2, axis=2)
    inter_cluster_dist = np.sum(cen_dists) / (K * (K - 1))
    return inter_cluster_dist