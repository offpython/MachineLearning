import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([0, 10, 20, 30, 40])
print(f'x shape: {x.shape}')
print(f'y shape: {y.shape}', '\n')

X, Y = np.meshgrid(x,  y)
print(X, '\n')
print(Y)
print(f'x shape: {X.shape}')
print(f'y shape: {Y.shape}')