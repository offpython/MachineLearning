# Step.2 For loop 모두 없애기

from time import time
import numpy as np
from numpy.random import randint

# (a,) shape
train_ds = randint(0, 10, (6000, 5))
test_ds = randint(0, 10, (1000, 5))

start_time = time()
for test_sample in test_ds:
    for train_sample in train_ds:
        dist = np.sum((train_sample - test_sample)**2)

end_time = time()
elapsed_time1 = end_time - start_time
print(f"{elapsed_time1 = }")

start_time = time()
for test_sample in test_ds:
    dists = np.sum((test_sample - train_ds)**2, axis=1)
    # test_sample: (5,)
    # train_ds: (6000, 5)

end_time = time()
elapsed_time2 = end_time - start_time
print(f"{elapsed_time2 = }")

#####
start_time = time()
train_ds = train_ds.reshape(6000, 1, 5)
test_ds = test_ds.reshape(1, 1000, 5)
dists = np.sum((train_ds - test_ds)**2, axis=2)
end_time = time()
elapsed_time3 = end_time - start_time
print(f"{elapsed_time3 = }")

print(f"time ratio: {elapsed_time1 / elapsed_time2}")
print(f"time ratio: {elapsed_time1 / elapsed_time3}")
print(f"time ratio: {elapsed_time2 / elapsed_time3}")