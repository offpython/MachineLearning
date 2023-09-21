# Random한 값 만들기
import numpy as np

# Random Integer
vec = np.random.randint(0, 10, (10,))
mat = np.random.randint(0, 10, (2, 3))
print(vec, '\n')
print(mat, '\n')

# Uniform Distribution에서 뽑기
vec1 = np.random.randint(0, 10, (10,))
vec2 = np.random.uniform(0, 10, (10,))
print(vec1, '\n')
print(vec2, '\n')

# np.random.normal
# 평균이 0이고, 표준편차가 2인 정규분포
data1 = np.random.normal(loc=0, scale=2, size=(100,))
print(data1)


