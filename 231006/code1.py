import numpy as np
import matplotlib.pyplot as plt

def get_y(x): return (1/10) * x**2
def get_dy_dx(x): return (1/5) * x

function_x = np.linspace(-5, 5, 100)
function_y = (1/10) * function_x**2

x = 3; y = get_y(x)
x = x - get_dy_dx(x)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(function_x, function_y)
ax.scatter(x,  y, c='r', s=100)

ax.tick_params(labelsize=15)
plt.show()

