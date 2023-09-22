# Step.1 모든 x-y 구하기


import numpy as np

data1 = np.arange(5)
data2 = np.arange(6)
print(f"data1: {data1.shape} -> {data1}")
print(f"data2: {data2.shape} -> {data2}\n")

data1 = data1.reshape(5, 1)
data2 = data2.reshape(1, 6)
total_sum = data1 - data2

print(f"data1: {data1.shape}\n{data1}")
print(f"data2: {data2.shape}\n{data2}\n")
print(total_sum)