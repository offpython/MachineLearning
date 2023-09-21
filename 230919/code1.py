# np.linspace
import numpy as np

# 0부터 20까지 5개의 숫자
print(np.linspace(0, 20, 5))
# 0부터 100까지 4개의 숫자
print(np.linspace(0, 100, 4))

# np.linspace와 그래프
import matplotlib.pyplot as plt

function_x = np.linspace(-3, 3, 100)
function_y = function_x**2

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(function_x, function_y)

ax.tick_params(labelsize=15)
fig.tight_layout()
plt.show()

# 연습.1 y = x2 + 2의 그래프를 [-2, 1]의 범위에 대해 그리세요.
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.exp(x)

fig, ax = plt.subplots(figsize=(10, 5))
ax.axhline(y=0, color='gray') # y축 시각화
ax.axvline(x=0, color='gray') # x축 시각화

ax.plot(x, y)
plt.show()

