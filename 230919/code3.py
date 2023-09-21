# 수학 함수들
import numpy as np

# 수학에서 사용되는 함수: log, exp, sin, cos, tan
# 넘파이에서 제공하는 수학 함수: np.log, np.exp, np.sin, np.cos, np.tan

# 3.141592(원주율) = np.pi
# 2.718(자연 상수) = np.e
print(np.pi) # 3.141592653589793
print(np.e) # 2.718281828459045

# 그래프
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y)

ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')

ax.tick_params(labelsize=15)
fig.tight_layout()
plt.show()
