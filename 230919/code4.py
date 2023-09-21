# Random Dataset 만들기 연습

# 방법1
import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt

np.random.seed(0)

n_sample = 300
x = normal(loc=0, scale=3, size=(n_sample,))
y = normal(loc=-2, scale=1, size=(n_sample,))

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(x, y)

ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')

ax.tick_params(labelsize=15)
plt.show()

# 방법2 (추천)
import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt

n_sample = 100
x = normal(loc=0, scale=3, size=(n_sample,))
y = normal(loc=-2, scale=1, size=(n_sample,))

# print(x, '\n')
# print(y, '\n')

dataset = np.hstack([x.reshape(n_sample, 1), y.reshape(n_sample, 1)])
print(dataset.shape)

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(dataset[:, 0], dataset[:, 1])

ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')

ax.tick_params(labelsize=15)
plt.show()