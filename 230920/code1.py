# 두 백터 사이의 distance 구하기

import numpy as np

np.random.seed(0)

dimension = 2
x = np.random.randint(-5, 6, (dimension,))
y = np.random.randint(-5, 6, (dimension,))
print(f"x: {x}")
print(f"x: {y}\n")

# 공식
euclidean_dist = np.sqrt(np.sum((x-y)**2))  # L2 distance
manhattan_dist = np.sum(np.abs((x-y)))      # L1 distance = Taxicab distnace


# 1. euclidean 설명
#원소별 뺄셈
distance = x - y
print(distance)
#제곱
distance =  distance ** 2
print(distance)
#합
distance = np.sum(distance)
print(distance)
#루트
distance = np.sqrt(distance)
print(distance)

distance = np.sqrt(np.sum((x-y)**2))
print(distance)

# 2. manhattan distance 설명
distance = x - y
print(distance)

distance = np.abs(distance)
print(distance)

distance = np.sum(distance)
print(distance)

distance = np.sum(abs(x-y))