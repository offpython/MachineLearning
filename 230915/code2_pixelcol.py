import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATASET_PATH = 'mnist_data'
dataset = pd.read_csv(os.path.join(DATASET_PATH, 'mnist_binary.csv'), index_col=0)
prior = pd.read_csv(os.path.join(DATASET_PATH, 'prior.csv'))

pixels = dataset.columns

def cal_likelihoods(dataset, target_pixel):
    n_total = dataset.shape[0]
    likelihoods = {}

    for label_value in dataset['label'].unique():
        subset = dataset[dataset['label'] == label_value]
        n_one = (subset[target_pixel] == 1).sum()
        n_zero = (subset[target_pixel] == 0).sum()
        likelihoods[label_value] = {
            '1': n_one / n_total,
            '0': n_zero / n_total
        }

    likelihoods = pd.DataFrame(data=likelihoods).sort_index()

    return likelihoods

print(cal_likelihoods(dataset, '8x8'), '\n')

label = dataset['label']
def combine_likelihoods(target_pixel):

    n0 = dataset[(label == 0)]
    n1 = dataset[(label == 1)]
    n2 = dataset[(label == 2)]
    n3 = dataset[(label == 3)]
    n4 = dataset[(label == 4)]
    n5 = dataset[(label == 5)]
    n6 = dataset[(label == 6)]
    n7 = dataset[(label == 7)]
    n8 = dataset[(label == 8)]
    n9 = dataset[(label == 9)]

    n0_likelihoods = cal_likelihoods(n0, target_pixel)
    n1_likelihoods = cal_likelihoods(n1, target_pixel)
    n2_likelihoods = cal_likelihoods(n2, target_pixel)
    n3_likelihoods = cal_likelihoods(n3, target_pixel)
    n4_likelihoods = cal_likelihoods(n4, target_pixel)
    n5_likelihoods = cal_likelihoods(n5, target_pixel)
    n6_likelihoods = cal_likelihoods(n6, target_pixel)
    n7_likelihoods = cal_likelihoods(n7, target_pixel)
    n8_likelihoods = cal_likelihoods(n8, target_pixel)
    n9_likelihoods = cal_likelihoods(n9, target_pixel)

    likelihoods = pd.concat([n0_likelihoods, n1_likelihoods, n2_likelihoods, n3_likelihoods, n4_likelihoods,
                             n5_likelihoods, n6_likelihoods, n7_likelihoods, n8_likelihoods, n9_likelihoods],
                                 axis=1)
    likelihoods.columns = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return likelihoods

print(combine_likelihoods('8x8'))

print(dataset.columns[0:], '\n')

def get_total_likelihoods(dataset):
    total_likelihoods = []
    attributes = dataset.columns[1:]

    for attribute in attributes:
        likelihoods = combine_likelihoods(attribute)
        total_likelihoods.append(likelihoods)

    total_likelihoods = pd.concat(total_likelihoods, axis = 0)

    return total_likelihoods

total_likelihoods = get_total_likelihoods(dataset).fillna(0)

print(dataset.columns)
print(total_likelihoods)
total_likelihoods.to_csv(os.path.join(DATASET_PATH, 'total_likelihoods.csv'))
print(dataset.columns[1:])

'''
230915 강사님 설명
우리의 목표 : 픽셀 정보를 가지고 hypo 784개 예측하기
likelihood : 클래스가 k로 주어졌을 때 각 픽셀이 어두울/밝을 확률 --> P(imageXij = 1 | Ck)

posterior : 이미지가 들어왔을 때(각 픽셀 값들이 들어왔을 때) -> 5일 확률 P(C5 | image) / P(image)인데 
P(image)는 포스테리어의 모든 계산에서 같은 분모를 계산하기 때문에 계산하지 않아도 괜찮음. 어차피 약분

이미지가 들어왔을 때 0일지, 1일지, 2일지, ... , 9일지의 posterior를 계산해서 가장 큰 확률을 선택

P(C5 | image)
여기서 image = P(C5) * P(image|C5)    인데 P(C1)이나 P(C5)나 값이 비슷(prior가 거의 동일하기 때문에)

따라서 포스테리어는 라이클리후드와 비례한다
P(C5 | image) 비례 P(imageXij = 1 | Ck)



'''

