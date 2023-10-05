# Outlook의 Information Gain 구하기

import pandas as pd

from utils import cal_entropy

dataset = pd.read_csv('play_tennis.csv', index_col=0)
print(dataset.head(), '\n')

H_dataset = cal_entropy(dataset)

feature_name = 'outlook'
feature_uniques = dataset[feature_name].unique()

H_feature = 0
n_total_samples = len(dataset)
for feature_unique in feature_uniques:
    bool_series = (dataset[feature_name] == feature_unique)
    feature_df = dataset[bool_series]

    H = cal_entropy(feature_df)
    n_feature_samples = len(feature_df)
    H_feature += (n_feature_samples/n_total_samples)

    H = cal_entropy(feature_df)

info_gain = H_dataset - H_feature

