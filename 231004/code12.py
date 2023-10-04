from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier

TRAIN_TEST_RATIO = 0.8
X, y = make_blobs(cluster_std=2, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    train_size=TRAIN_TEST_RATIO,
                                                    random_state=0)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

train_acc = classifier.score(X_train, y_train)
test_acc = classifier.score(X_test, y_test)
print(f"train acc: {train_acc}")
print(f"test acc: {test_acc}")