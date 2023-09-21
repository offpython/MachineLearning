# broaacasting

import numpy as np

A = np.arange(12).reshape(6, 2)
print(f"A: {A.shape}\n{A}\n")

B = np.array([10, 100])
print(f"B: {B.shape}\n{B}\n")

C = A + B
print(f"A + B:{C.shape}\n{C}")