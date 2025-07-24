import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x1, x2, m=10):
    return -(np.sin(x1) * (np.sin(1 * x1**2 / np.pi)**(2*m)) + np.sin(x2) * (np.sin(2 * x2**2 / np.pi)**(2*m)))

x1_min, x1_max = 0.0, np.pi
x2_min, x2_max = 0.0, np.pi
test_point = (2.20, 1.57)
step = 0.05

x1 = np.arange(x1_min, x1_max, step)
x2 = np.arange(x2_min, x2_max, step)
X1, X2 = np.meshgrid(x1, x2)
Y = f(X1, X2)

y_test = f(test_point[0], test_point[1])

fig = plt.figure(figsize=(16, 12))
fig.suptitle(f'Графики функции f(x1, x2)\nТестовая точка: ({test_point[0]}, {test_point[1]}), f(x1, x2) = {y_test:.4f}',
             fontsize=14)

ax1 = fig.add_subplot(221, projection='3d')
surf1 = ax1.plot_surface(X1, X2, Y, cmap='viridis', edgecolor='none')
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('y = f(x1, x2)')
ax1.set_title('3D поверхность (изометрический вид)')
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)

ax2 = fig.add_subplot(222, projection='3d')
surf2 = ax2.plot_surface(X1, X2, Y, cmap='viridis', edgecolor='none')
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
ax2.set_zlabel('y = f(x1, x2)')
ax2.set_title('3D поверхность (вид сверху)')
ax2.view_init(elev=90, azim=0)  # Вид сверху
fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)

x2_test = test_point[1]
ax3 = fig.add_subplot(223)
ax3.plot(x1, f(x1, x2_test * np.ones_like(x1)))
ax3.set_xlabel('x1')
ax3.set_ylabel(f'y = f(x1, {x2_test})')
ax3.set_title(f'График функции при x2 = {x2_test}')
ax3.grid(True)

x1_test = test_point[0]
ax4 = fig.add_subplot(224)
ax4.plot(x2, f(x1_test * np.ones_like(x2), x2))
ax4.set_xlabel('x2')
ax4.set_ylabel(f'y = f({x1_test}, x2)')
ax4.set_title(f'График функции при x1 = {x1_test}')
ax4.grid(True)

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()
