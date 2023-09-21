# Sort와 Argsort

import numpy as np
np.random.seed(0)

data = np.random.randint(0, 100, (10,))
print(data, '\n')

print(np.sort(data))
print(np.argsort(data))