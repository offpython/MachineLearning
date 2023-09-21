import numpy as np
np.random.seed(0)

data=np.random.randint(0, 100, (10,))
print(data, '\n')

# np.sort는 작은 값부터 정렬
# np.argsort는 작은 값부터 큰 값까지의 인덱스
print(np.sort(data),'\n')
print(np.argsort(data), '\n')
