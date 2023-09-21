import pandas as pd
import os

DATA_PATH = 'mnist_data'
FILE_TYPES = ['train', 'test']
THRESHOLD = 100

for file_type in FILE_TYPES:
    load_file_name = f'mnist_{file_type}.csv'
    save_file_name = f'mnist_{file_type}_binary.csv'

    load_file = os.path.join(DATA_PATH, load_file_name)
    save_file = os.path.join(DATA_PATH, save_file_name)

    dataset = pd.read_csv(load_file)

    labels, imgs = dataset.iloc[:, 0], dataset.iloc[:, 1:].copy()

    imgs[imgs < THRESHOLD] = 0
    imgs[imgs >= THRESHOLD] = 1

    dataset_binary = pd.concat([labels, imgs], axis=1)
    dataset_binary.to_csv(save_file)
