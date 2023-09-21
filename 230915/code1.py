import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATASET_PATH = 'mnist_data'
dataset = pd.read_csv(os.path.join(DATASET_PATH, 'mnist_train.csv'))

labels = dataset['label']
images = dataset.iloc[:, 1:].copy()

# images[images <= 100] = 0
# images[images > 100] = 1

dataset = pd.concat([labels, images], axis=1)
dataset.to_csv(os.path.join(DATASET_PATH, 'mnist_binary.csv'))

print(labels.shape)
print(images.shape)

SAMPLE_INDEX = 0 # 샘플데이터 한 줄 가져오슈

DATASET_PATH = 'mnist_data'
dataset = pd.read_csv(os.path.join(DATASET_PATH, 'mnist_binary.csv'), index_col=0)

sample = dataset.iloc[SAMPLE_INDEX]
label = sample['label']
# print(sample)
# Series를 (28, 28)의 행렬로 바꾸는 연산
img = np.array(sample.drop('label')).reshape(28, 28)

fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(img, cmap='gray')
ax.set_title(f"Class {label}", fontsize=30)
ax.axis('off')
plt.show()



''' prior를 구해보자 '''

labels_unique_values = labels.unique()
# print(labels_unique_values)

prior_probs = dict()

n_total = labels.count() # 10000
for unique_value in labels_unique_values:
    hypo = (labels == unique_value)
    n_hypo = hypo.sum()

    hypo_prior = n_hypo / n_total
    prior_probs[unique_value] = hypo_prior

prior_series = pd.Series(name='prior', data=prior_probs).sort_index()
prior_series.to_csv(os.path.join(DATASET_PATH, 'prior.csv'))
print(prior_series)

prior = pd.read_csv(os.path.join(DATASET_PATH, 'prior.csv'))

print(prior_series.index)
