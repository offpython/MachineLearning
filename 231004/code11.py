import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

dataset = load_wine()
X, y = dataset.data, dataset.target

classifier_names = ['knn', 'centroid', 'gnb', 'dt']
classifiers = [KNeighborsClassifier(n_neighbors=5),
               NearestCentroid(),
               GaussianNB(),
               DecisionTreeClassifier()]
accs = []
for classifier in classifiers:
    classifier.fit(X, y)
    acc = classifier.score(X, y)
    accs.append(acc)

fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(classifier_names, accs)
ax.tick_params(labelsize=15)
ax.set_ylim([0.6, 1.05])
plt.show()