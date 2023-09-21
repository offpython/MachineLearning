import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_PATH = 'mnist_data'
DATA_FILE_NAME = 'mnist_train.csv'

data_file = os.path.join(DATA_PATH, DATA_FILE_NAME)
print(f"File existence test -> {os.path.exists(data_file)}")

dataset_df = pd.read_csv(data_file, index_col=0)
print(dataset_df)

y = dataset_df.index.to_numpy()
X = dataset_df.drop.to_numpy()

k_list = list(range(1, 51, 1))
acc_dict = {}

for K in k_list:
    n_corrects = 0
    for X_, y_ in zip(X, y):
        dists = np.sum((X - X_)**2, axis=1)

        sorted_indices = np.argsort(dists)
        closest_indices = sorted_indices[:K]
        closest_classes = y[closest_indices]

        uniques, cnts = np.unique(closest_classes, return_counts=True)
        pred = uniques[np.argmax(cnts)]

        if pred == y_: n_corrects += 1

    acc = n_corrects / len(y)
    acc_dict[K] = acc
    print(f"K: {K} -> Acc: {acc:.4f}")

print(acc_dict)

fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(acc_dict.keys(), acc_dict.values())

ax.set_ylim([0.92, 1.01])
plt.show()