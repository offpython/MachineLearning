import numpy as np
import pandas as pd

def cal_entropy(df):
    n_total_samples = len(df)
    class_cnts = df['play'].value_counts()

    probs = class_cnts / n_total_samples
    infos = -np.log2(probs)

    H = np.sum(probs * infos)
    return H


def cal_info_gain(feature_name, H_dataset, dataset):
    feature_uniques = dataset[feature_name].unique()

    H_feature = 0
    n_total_samples = len(dataset)
    for feature_unique in feature_uniques:
        bool_series = (dataset[feature_name] == feature_unique)
        feature_df = dataset[bool_series]

        H = cal_entropy(feature_df)
        n_feature_samples = len(feature_df)

        H_feature += (n_feature_samples / n_total_samples) * H

    info_gain = H_dataset - H_feature
    return info_gain

dataset = pd.read_csv('play_tennis.csv', index_col=0)

H_dataset = cal_entropy(dataset)
print(f"dataset entropy: {H_dataset}\n")

feature_names = dataset.columns[:-1]
info_gains = []
for feature_name in feature_names:
    info_gain = cal_info_gain(feature_name, H_dataset, dataset)
    info_gains.append(info_gain)
    print(f"{feature_name} ---> {info_gain}")

print("\nBest Feature:", feature_names[np.argmax(info_gains)])