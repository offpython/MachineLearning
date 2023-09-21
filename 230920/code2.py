# Sort와 Argsort

import numpy as np
np.random.seed(0)

data=np.random.randint(0, 100, (10,))
print(data, '\n')

# np.sort는 작은 값부터 정렬
# np.argsort는 작은 값부터 큰 값까지의 인덱스
print(np.sort(data),'\n')
print(np.argsort(data), '\n')


## 거리가 얼마나 가까운게 중요한게 아니라, 가까운 지점의 인덱스가 어딘지를 알아내야함 => argsort로 인덱스 찾기