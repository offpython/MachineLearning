
# ndarray 의 ndim
import numpy  as np

# (a, ) shape
A = np.random.randint(0, 10, (20, ))
print(A.ndim)
'''
[3 2 3 8 0 1 1 5 9 1 8 6 6 5 1 8 9 6 4 8] => 20차원 1차 텐서 
'''
# (a, b) shape
B = np.random.randint(0, 10, (4, 5))
print(B.ndim)
'''
[[8 8 7 7 8]
 [1 5 4 8 4]
 [5 1 0 9 4]
 [0 9 8 7 7]] => 20차원 2차 텐서
'''
