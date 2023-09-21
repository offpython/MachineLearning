# Numpy의 행렬에서 행, 열을 가져올 때 주의점 -> 백터형식으로 가져옴
import numpy as np

A = np.arange(12).reshape(3, 4)
print(f'A: {A.shape}\n{A}\n')

print(A[0])
print(A[0].shape)
print(A[1].shape)
print(A[2].shape, '\n')

print(A[:, 0])
print(A[:, 0].shape)
print(A[:, 1].shape)
print(A[:, 2].shape)
print(A[:, 3].shape, '\n')



