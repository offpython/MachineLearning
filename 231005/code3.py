# Outlook 중에서 Sunny인 부분만 뽑아보기

import pandas as pd
from utils import cal_entropy

dataset = pd.read_csv('play_tennis.csv', index_col=0)
print(dataset, '\n')

feature_name = 'outlook'
feature_uniques = dataset[feature_name].unique()

bool_series = dataset[feature_name] == feature_uniques[0]
feature_df = dataset[bool_series]

print(feature_name , '\n')
print(feature_uniques , '\n')
print(feature_df)

# Outlook으로 나눠지는 경우들의 entropy
for feature_unique in feature_uniques:
    bool_series = (dataset[feature_name] == feature_unique)
    feature_df = dataset[bool_series]
    H = cal_entropy(feature_df)
