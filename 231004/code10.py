import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

dataset = load_wine()
X, y = dataset.data, dataset.target

classifiers = {
    'knn': KNeighborsClassifier(n_neighbors=5),
    'centroid': NearestCentroid(),
    'gnb': GaussianNB(),
    'dt': DecisionTreeClassifier()
}

acc_dict = {}
for classifier_name, classifier in classifiers.items():
    classifier.fit(X, y)
    acc = classifier.score(X, y)
    acc_dict[classifier_name] = acc

fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(acc_dict.keys(), acc_dict.values())
ax.tick_params(labelsize=15)
ax.set_ylim([0.6, 1.05])
plt.show()
