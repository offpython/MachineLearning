import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier

k_list = list(range(1, 51))
print(k_list)

dataset = load_wine()
X, y = dataset.data, dataset.target

k_acc_dict = {}
for k in k_list:
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(X, y)

    acc = classifier.score(X, y)
    k_acc_dict[k] = acc

fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(k_acc_dict.keys(), k_acc_dict.values())

ax.tick_params(labelsize=15)
ax.set_ylim([min(k_acc_dict.values()) - 0.1, 1.05])
ax.set_title("KNN on Wine Dataset", fontsize=25)
ax.set_xlabel("K", fontsize=20)
ax.set_ylabel("Acc", fontsize=20)

fig.tight_layout()
plt.show()