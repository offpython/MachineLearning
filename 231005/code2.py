# Dataset의 Entropy 구하기

import numpy as np
import pandas as pd

dataset = pd.read_csv('play_tennis.csv')

n_total_samples = len(dataset)
class_cnts = dataset['play'].value_counts()

probs = class_cnts / n_total_samples
infos = -np.log2(probs)

H = np.sum(probs * infos)
print(f"Entropy: {H}")

# def cal_entropy(df):
def cal_entropy(df):
    n_total_samples = len(df)
    class_cnts = df['play'].value_counts()

    probs = class_cnts / n_total_samples
    infos = -np.log2(probs)

    H = np.sum(probs * infos)
    return H

